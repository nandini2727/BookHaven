from .models import Wishlist
from cart.models import Cart
from django.db import models

def cart_wishlist_counts(request):
    if request.user.is_authenticated:
        # Count wishlist items
        wishlist_count = Wishlist.objects.filter(user=request.user).count()

        # Count cart items
        cart = Cart.objects.filter(user=request.user).first()
        cart_count = cart.items.aggregate(total_items=models.Sum('quantity'))['total_items'] if cart else 0
        cart_count=0 if cart_count==None else cart_count
        return {
            'wishlist_count': wishlist_count,
            'cart_count': cart_count
        }
    return {
        'wishlist_count': 0,
        'cart_count': 0
    }
