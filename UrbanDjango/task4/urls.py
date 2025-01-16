from django.contrib import admin
from django.urls import path, include
from .views import index, shop, cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),  # Главная страница
    path('shop/', shop, name='shop'),  # Магазин
    path('cart/', cart, name='cart'),  # Корзина
]

