from django.http import HttpRequest
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing

# Create your views here.
def index(request: HttpRequest):
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6) #, allow_empty_first_page=True)
    page_number = request.GET.get('page')
    listing_obj = paginator.get_page(page_number)

    # listings = [listing for listing in listings if bool(listing.is_published)]
    print('listings', listing_obj)
    context = {
        'listings': listing_obj
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = Listing.objects.filter(pk=listing_id)

    print(listing_id)
    print(listing)
    context = {'listing': listing}
    
    return render(request, 'listings/listing.html', context)
def search(request):
    return render(request, 'listings/search.html')