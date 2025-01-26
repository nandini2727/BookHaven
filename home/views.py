from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.template import loader
from books.models import *
from .models import Contact
from django.db.models import Q
from books.utils import track_browsing_history
from .utils import get_browsing_history
from django.conf.urls import handler404
from django.shortcuts import render
from cart.utils import recommend_books
from cart.models import Cart
# Custom 404 handler
def custom_404_view(request, exception):
    return render(request, "404.html", status=404)

handler404 = custom_404_view

def home(request):
    categories = Category.objects.all()
    featured_books = []
    latest_arrival=[]
    for category in categories:
        book = Book.objects.filter(category=category).order_by('popularity').first()  # Get the first book in the category
        latest_book=Book.objects.filter(category=category).order_by('-created_at').first()
        if book:
            featured_books.append(book)
        if latest_book:
            latest_arrival.append(latest_book)
    browsing_history = get_browsing_history(request)
    context={
        "categories":categories,
        "featured_books":featured_books,
        "latest_arrival":latest_arrival,
        'browsing_history': browsing_history
        }
    
    return render(request,"home.html",context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the data to the database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        ) 
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  

    return render(request, "contact.html")
           

def shop(request):
    query = request.GET.get('q', '')  # Get the search query from the GET parameters
    if query:
        # Filter books by name or author (case-insensitive match)
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        # If no query, show all books
        books = Book.objects.all()

    category_filter = request.GET.get('category', 'all')
    format_filter = request.GET.get('format')
    sort_filter = request.GET.get('sort', '')
    price_max = request.GET.get('price_max', None)
    rating_filter = request.GET.getlist('ratings')

    # Apply filters
    if category_filter != 'all':
        books = books.filter(category__name=category_filter)

    if format_filter == 'ebook':
        books = books.filter(is_ebook=True)
    elif format_filter == 'hardcopy':
        books = books.filter(is_hardcopy=True)

    if price_max:
        books = books.filter(price__lte=price_max)

    if rating_filter:
        books = books.filter(rating__in=rating_filter)

    # Apply sorting
    if sort_filter == 'popularity':
        books = books.order_by('-popularity')
    elif sort_filter == 'price-low':
        books = books.order_by('price')
    elif sort_filter == 'price-high':
        books = books.order_by('-price')
    elif sort_filter == 'newest':
        books = books.order_by('-created_at')

    # Pagination
    paginator = Paginator(books, 9)  
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    # Get categories for the filter section
    categories = Category.objects.all()

    context = {
        'books': page_obj,
        'categories': categories,
        'applied_filters': {
            'category': category_filter,
            'format': format_filter,
            'sort': sort_filter,
            'price_max': price_max,
            'ratings': rating_filter,
        },
    }
    return render(request, 'shop.html', context)

def product(request,book_id):
    book = get_object_or_404(Book, id= book_id)
    track_browsing_history(request, book_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        recommended_books=recommend_books(cart)
    else:
        recommended_books=[]
    # Pass the book to the template for rendering
    return render(request, 'product.html', {'book': book, "recommended_books":recommended_books})


