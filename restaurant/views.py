from django.shortcuts import render
import time
import random

# Create your views here.
def main(request):
    template_name = 'restaurant/main.html'
    return render(request, template_name)

def order(request):
    template_name = 'restaurant/order.html'

    todays_special = [
        'Coffee',
        'Pizza',
        'Donuts',
    ]

    x = random.randint(0,2)
    context = {
        'special': todays_special[x]
    }
    return render(request, template_name, context)

def confirmation(request):
    template_name = 'restaurant/confirmation.html'
    
    if request.POST:
        if 'cheese' not in request.POST:
            cheeses = 'Ricotta'
        else:
            cheeses = request.POST['cheese']
        toppings = request.POST.getlist('topping')

        special = False
        
        if 'special' in request.POST:
            special = True
        
        total = 2 + len(toppings) * 2
        if special:
            total += 3
        
    minutes = random.randint(30,60)
    readytime = time.ctime(time.time() + minutes * 60)
    context = {
        'cheeses_order': cheeses,
        'toppings_order': toppings,
        'cost': total,
        'special_order': '',
        'time': readytime,
    }

    if special:
        context['special_order'] = 'Special'

    return render(request, template_name, context)