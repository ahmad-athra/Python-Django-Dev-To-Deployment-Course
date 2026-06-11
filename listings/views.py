from django.shortcuts import render

from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.all()
    # listings = [listing for listing in listings if bool(listing.is_published)]
    print('listings', listings)
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request ): #,listing_id):
    return render(request, 'listings/listing.html')
def search(request):
    return render(request, 'listings/search.html')