from django.shortcuts import get_object_or_404,render
from django.core.paginator import  PageNotAnInteger ,EmptyPage , Paginator
from .models import Listing
from .chosices import bedroom_choices , price_choices , state_choices

def listing(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,5)
    page_num = request.GET.get('page')
    paged_listing = paginator.get_page(page_num)
    
    content = {
        "listing": paged_listing,
    }
    return render(request, 'listing/listing.html',content)

def listings(request,listing_id):
    listings = get_object_or_404(Listing,pk=listing_id)

    content = {
        "list_id":listings
    }
    return render(request, 'listing/listings.html',content)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

        
    key_search = {
    "last_list": listings,
     "bedrooms": bedroom_choices,
     "price": price_choices,
     "state": state_choices ,  
     "listing" : queryset_list,
     "values": request.GET
    }

    return render(request, 'listing/search.html',key_search)
