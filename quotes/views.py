from django.shortcuts import render

# Create your views here.
import random

quotes = [
    'No, I am your father.',
    'I find your lack of faith disturbing.',
    'Be careful not to choke on your aspirations.',
]

images = [
    'quotes/images/img1.jpeg',
    'quotes/images/img2.jpeg',
    'quotes/images/img3.jpeg',
]

def quote(request):
    template_name = "quotes/quote.html"
    x = random.randint(0,2)
    y = random.randint(0,2)

    context = {
        'chosen_quote': quotes[x],
        'chosen_image': images[y],
    }

    return render(request, template_name, context)

def show_all(request):
    template_name = "quotes/showall.html"

    context = {
        'all_quotes': quotes,
        'all_images': images,
    }
    return render(request, template_name, context)

def about(request):
    template_name = "quotes/about.html"
    return render(request, template_name)