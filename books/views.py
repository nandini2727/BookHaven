from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Wishlist

# View to display the wishlist
@login_required(login_url="signin")
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

# Add a book to the wishlist
@login_required(login_url="signin")
def add_to_wishlist(request, book_id):
    book = Book.objects.get(id=book_id)
    if not Wishlist.objects.filter(user=request.user, book=book).exists():
        Wishlist.objects.create(user=request.user, book=book)
    return redirect('wishlist')  # Redirect to the wishlist view

# Remove a book from the wishlist
@login_required(login_url="signin")
def remove_from_wishlist(request, book_id):
    wishlist_item = Wishlist.objects.get(user=request.user, book_id=book_id)
    wishlist_item.delete()
    return redirect('wishlist')  # Redirect to the wishlist view
