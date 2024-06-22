from django.urls import path
from .views import index, cart, checkout, contact, detail, shop

urlpatterns = [
    path('', index, name='index'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('contact/', contact, name='contact'),
    path('detail/', detail, name='detail'),
    path('shop/', shop, name='shop'),
]