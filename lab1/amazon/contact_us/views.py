from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.
def contactpage(request):
    # return  HttpResponse('Hello from Contact Page')
    return render(request, 'contact_us.html')