from django.http import HttpRequest
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from realtors.models import Realtor
from django.shortcuts import get_object_or_404
from .choices import bedroom_choices,price_choices, state_choices

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
    # listing = Listing.objects.get(pk=listing_id)
    # context = {'listing': listing}

    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    
    return render(request, 'listings/listing.html', context)

def search(request: HttpRequest):
    # ?keywords=aaaa
    # &city=Salem
    # &state=AZ
    # &bedrooms=1
    # &price=100000
    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET and request.GET['keywords']:
        queryset_list = queryset_list.filter(description__icontains=request.GET['keywords'])

    if 'city' in request.GET and request.GET['city']:
        # not case sensetive "iexact"
        queryset_list = queryset_list.filter(city__iexact=request.GET['city'])

    if 'state' in request.GET and request.GET['state']:
        queryset_list = queryset_list.filter(state__iexact=request.GET['state'])

    if 'bedrooms' in request.GET and request.GET['bedrooms']:
        queryset_list = queryset_list.filter(bedrooms__lte=request.GET['bedrooms'])

    if 'price' in request.GET and request.GET['price']:
        queryset_list = queryset_list.filter(price__lte=request.GET['price'])

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET,
    }
    params = request.GET.get('')
    return render(request, 'listings/search.html', context)