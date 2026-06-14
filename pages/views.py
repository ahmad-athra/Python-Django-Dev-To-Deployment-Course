from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from listings.models import Listing
from realtors.models import Realtor

def index(request):
     latest_listing  = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

     context = {
          'listings': latest_listing
     }
     return render(request, 'pages/index.html', context)

def about(request):
     realtors = Realtor.objects.order_by('-hire_date')

     mvp = Realtor.objects.all().filter(is_mvp=True)
     context = {
          'realtors': realtors,
          'mvp': mvp,

     }

     return render(request, 'pages/about.html', context)