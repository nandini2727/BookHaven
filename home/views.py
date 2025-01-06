from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.template import loader
from books.models import *
from .models import Contact

def home(request):
    return render(request,"home.html")
    # template=loader.get_template('home.html')
    # return HttpResponse(template.render())

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
        return redirect('contact')  # Replace 'contact' with the name of your URL pattern

    return render(request, "contact.html")
           

def shop(request):
    categories = Category.objects.all()

    # Get the selected filters from GET request
    selected_category = request.GET.get('category', None)
    selected_format = request.GET.get('format', 'all')
    price_range = request.GET.get('price', 100000)
    sort_by = request.GET.get('sort_by', 'popularity')
    books = Book.objects.all()
    # Filter by format
    # if selected_format != 'all':
    #     books = Book.objects.filter(format=selected_format)  # Assuming 'format' is a field in your model
    # else:
    #     books = Book.objects.all()

    # Filter by category
    if selected_category:
        books = books.filter(category__id=selected_category)

    # Filter by price range
    books = books.filter(price__lte=price_range)

    # Sorting logic
    if sort_by == 'price-low':
        books = books.order_by('price')
    elif sort_by == 'price-high':
        books = books.order_by('-price')
    elif sort_by == 'newest':
        books = books.order_by('-created_at')
    else:  # Default sort by popularity
        books = books.order_by('-popularity')

    paginator = Paginator(books, 12)  # Show 10 books per page
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    context = {
        'books': page_obj,
        'categories': categories,
        'selected_category': selected_category,
        # 'selected_format': selected_format,
        'price_range': price_range,
        'sort_by': sort_by,
    }

    return render(request, 'shop.html', context)

def signin(request):
    return render(request, "signin.html")

def signup(request):
    return render(request, "signup.html")


# def cart(request):
#     return render(request, "cart.html")

# def wishlist(request):
#     return render(request, "wishlist.html")
# def contact(request):
#     return render(request, "contact.html")