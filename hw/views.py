#file: hw/views.py

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request):
    '''Fund to respond to the "home" request.'''

    response_text = '''
    <html>
    <h1>Hello World!</h1>
    </html>
    '''

    return HttpResponse(response_text)