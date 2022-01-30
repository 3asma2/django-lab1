from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#querystring
#def Homepage(request):
    #return HttpResponse('Welcome {}'.format(request.GET['name']))

#parameter
def Welcomepage(request):
    return HttpResponse('<button><a href="/">home</a></button>'
                        '<button><a href="about">about</a></button>' 
                        '<button><a href="contact">contact</a></button>'
                        '</br>''<h1> Welcome to amazon</h1>''</br>'
                        '<img src="https://images-na.ssl-images-amazon.com/images/G/01/marketing/npa/HUB/v2/1921377_npa_hub_header_desktop_v2.png" width="100%" >')