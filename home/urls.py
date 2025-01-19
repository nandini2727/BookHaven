from django.urls import path
from . import views
from cart import views as cart_views
urlpatterns=[
    path('',views.home,name='home'),
    path('shop',views.shop,name='shop'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('contact',views.contact,name='contact'),
    path('product/<int:book_id>/',views.product,name="product"),
    path("delete_address/<int:address_id>/",cart_views.delete_address,name='delete_address'),
    path("checkout/", cart_views.checkout, name="checkout"),
    path("add-address/", cart_views.add_address, name="add_address"),
    path("order-success/<int:order_id>/", cart_views.order_success, name="order_success"),
]