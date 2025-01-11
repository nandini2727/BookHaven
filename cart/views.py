from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from books.models import Book
from django.http import JsonResponse
from django.utils.timezone import now
from .models import Coupon
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
