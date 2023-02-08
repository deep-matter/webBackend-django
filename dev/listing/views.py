from django.shortcuts import render
from django.core.paginator import  PageNotAnInteger ,EmptyPage
from .models import Listing

def listing(request):
    listings = Listing.objects.all() # 
    # Pagination= Paginator(listings,3)
    # page = request.GET.get('page')
    # paged_listing = Pagination(page)
    
    content = {
        "listing": listings,
    }
    return render(request, 'listing/listing.html',content)

def listings(request,listing_id):
    return render(request, 'listing/listings.html')

def search(request):
    return render(request, 'listing/search.html')
