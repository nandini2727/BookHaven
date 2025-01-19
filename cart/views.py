from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem,Address
from django.contrib import messages
from books.models import Book
from django.http import JsonResponse
from django.utils.timezone import now
from .models import Coupon,Order,OrderItem
import json
from .utils import recommend_books


@login_required(login_url="signin")
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_price = cart.total_price() 
    tax = total_price * Decimal(0.10)  # Calculate 10% tax
    total = total_price + tax  # Total = Subtotal + Tax
    # Coupon logic
    coupon_id = request.session.get('coupon_id')  # Check if a coupon is applied
    discount = Decimal(0)  # Default discount is 0
    coupon_code = None  # Default coupon code is None

    if coupon_id:
        try:
            coupon = Coupon.objects.get(id=coupon_id, active=True)
            if coupon.valid_from <= now() <= coupon.valid_to:  # Ensure the coupon is valid
                discount = (total_price * coupon.discount) / 100  # Calculate the discount amount
                coupon_code = coupon.code  # Store the applied coupon code
            else:
                del request.session['coupon_id']  # Remove invalid/expired coupon from session
        except Coupon.DoesNotExist:
            del request.session['coupon_id']  # Remove invalid coupon from session

    # Apply discount and calculate the final total
    total_price_after_discount = total_price - discount
    total = total_price_after_discount + tax  # Total = (Subtotal - Discount) + Tax

    #recommeded books
    recommended_books = recommend_books(cart)
    context = {
        'cart': cart,
        'tax': tax,
        'total': total,
        'discount': discount,  # Discount amount
        'total': total,  # Final total after discount and tax
        'coupon_code': coupon_code,  # Applied coupon code (if any)
        'recommended_books': recommended_books
    }
    return render(request, 'cart.html', context)


@login_required(login_url="signin")
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url="signin")
def remove_from_cart(request, book_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, book_id=book_id)
    cart_item.delete()
    return redirect('cart_view')


@login_required(login_url="signin")
def update_cart(request, book_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, book_id=book_id)

    if 'quantity' in request.POST:
        new_quantity = int(request.POST.get('quantity'))
        if new_quantity <= 0:
            # Remove the item if the quantity is zero or less
            cart_item.delete()
        else:
            # Update the quantity if it is greater than zero
            cart_item.quantity = new_quantity
            cart_item.save()

    return redirect('cart_view')


def apply_coupon(request):
    if request.method == "POST":
        data = json.loads(request.body)
        code = data.get("promo_code")  # Get the coupon code from the request
        try:
            coupon = Coupon.objects.get(code=code, active=True)
            if coupon.valid_from <= now() <= coupon.valid_to:
                # Store the coupon ID in the session
                request.session["coupon_id"] = coupon.id
                return JsonResponse({"success": True, "message": "Coupon applied successfully!"})
            else:
                return JsonResponse({"success": False, "message": "This coupon is expired."})
        except Coupon.DoesNotExist:
            return JsonResponse({"success": False, "message": "Invalid coupon code."})
    return JsonResponse({"success": False, "message": "Invalid request method."})


def clear_coupon(request):
    if "coupon_id" in request.session:
        del request.session["coupon_id"]
    return JsonResponse({"success": True, "message": "Coupon removed successfully!"})



@login_required(login_url='signin')
def checkout(request):
    # Get the cart associated with the current user
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    # Get all items in the user's cart
    cart_items = CartItem.objects.filter(cart=cart) if cart else []

    # Calculate the subtotal (sum of all cart item prices)
    subtotal = sum(item.total_price() for item in cart_items)

    # Example shipping cost (replace this logic as needed)
    shipping_cost = 50 if cart_items else 0

    # Calculate the total
    total = subtotal + shipping_cost

    # Get all addresses associated with the user
    addresses = Address.objects.filter(user=request.user)

    # Render the checkout page with the required context
    context = {
        "cart_items": cart_items,
        "addresses": addresses,
        "subtotal": subtotal,
        "shipping_cost": shipping_cost,
        "total": total,
    }

    if request.method == "POST":
        # Handle form submission (e.g., confirming an order)
        selected_address_id = request.POST.get("selected_address")
        payment_method = request.POST.get("payment_method")

        # Validate the selected address
        try:
            selected_address = Address.objects.get(id=selected_address_id, user=request.user)
        except Address.DoesNotExist:
            selected_address = None

        if not selected_address:
            context["error"] = "Please select a valid address."
            return render(request, "checkout.html", context)

        order = Order.objects.create(
            user=request.user,
            address=selected_address,
            payment_method=payment_method,
            total=total,
            created_at=now(),
        )

        # Create OrderItems
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                book_name=cart_item.book.title,
                category=cart_item.book.category,
                cover_image=cart_item.book.cover_image,
                price=cart_item.book.price,
            )

        # Clear the cart
        cart.items.all().delete()

        # Redirect to order confirmation page
        messages.success(request, "Your order has been placed successfully!")
        # Redirect to a success page or order confirmation
        return redirect("order_success",order_id=order.id)  # Replace with your success URL

    return render(request, "checkout.html", context)



@login_required(login_url='signin')
def add_address(request):
    if request.method == "POST":
        # Extract data from the request.POST dictionary
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip_code")
        address_line = request.POST.get("address")

        # Validate required fields
        if not all([name, phone, email, city, state, zip_code, address_line]):
            messages.error(request, "All fields are required. Please fill in all the details.")
            return redirect("checkout")  # Redirect back to checkout if validation fails

        # Save the address
        Address.objects.create(
            user=request.user,
            name=name,
            phone=phone,
            email=email,
            city=city,
            state=state,
            zip_code=zip_code,
            address=address_line,
        )

        messages.success(request, "Address added successfully!")
        return redirect("checkout")  # Redirect to checkout page after successful submission

    # If GET request, render the checkout page
    return redirect("checkout")

@login_required(login_url="signin")
def delete_address(request, address_id):
    address = Address.objects.get(id=address_id)
    address.delete()
    return redirect('checkout')

from django.shortcuts import render

def order_success(request, order_id):
    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect("home")

    context = {"order": order}
    return render(request, "order_successful.html", context)
