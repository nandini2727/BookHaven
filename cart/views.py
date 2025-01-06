from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from books.models import Book

@login_required(login_url="signin")
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_price = cart.total_price() 
    tax = total_price * Decimal(0.10)  # Calculate 10% tax
    total = total_price + tax  # Total = Subtotal + Tax
    context = {
        'cart': cart,
        'tax': tax,
        'total': total,
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
