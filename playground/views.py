from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request -> response
# Request Handler
# In some frameworks this is called action

def say_hello(request):
    return HttpResponse('Hello World')
    # return render(request, 'hello.html', {'name': 'Mehul'}) 
