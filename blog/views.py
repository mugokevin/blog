from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'homepage.html')
   # return HttpResponse("home page")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('about')