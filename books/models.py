from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_hardcopy = models.BooleanField(default=False)
    is_ebook = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    popularity = models.PositiveIntegerField(default=0)  # Number of times bought
    created_at = models.DateTimeField(default=now)  # Timestamp for sorting by newest
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0) 
    cover_image =  models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlists")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="wishlist_items")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')  # A user can only wishlist a book once

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.book.name}"


class BrowsingHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='browsing_history')
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Browsing History"

    def add_book(self, book):
        # Add the book to the history
        self.books.add(book)
        # Limit to the latest 15 books
        if self.books.count() > 15:
            oldest_book = self.books.first()  # Assuming ManyToManyField preserves order
            self.books.remove(oldest_book)
