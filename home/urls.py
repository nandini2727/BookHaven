from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('shop',views.shop,name='shop'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('contact',views.contact,name='contact'),
    path('cart',views.cart,name='cart'),
]