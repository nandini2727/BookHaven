from django.db import models
from django.utils.timezone import now

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
    ebook_file = models.FileField(upload_to='ebooks/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title
