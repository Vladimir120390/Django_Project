
from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = {
        'Игровая приставка PlayStation5': 'Купить',
        'The Witсher 3 Game of Year': 'Купить',
        'Assassins Creed. Collection': 'Купить',
}
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')


# Create your views here.
