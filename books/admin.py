from django.contrib import admin
from .models import Book,Category,Wishlist
# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'stock']
    list_filter = ['category', 'popularity']
    search_fields = ['title']
admin.site.register(Category)
admin.site.register(Wishlist)

