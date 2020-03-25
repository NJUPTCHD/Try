from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def other( request ):
    return HttpResponse("    你已经进入其他的页面了")