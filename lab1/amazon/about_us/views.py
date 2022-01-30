from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.
def aboutpage(request):
    # return HttpResponse("Hello from About") in case there is no html page and because he takes string

    return render(request, 'about_us.html')
