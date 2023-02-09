from django.shortcuts import render
from django.core.paginator import  PageNotAnInteger ,EmptyPage , Paginator
from .models import Listing

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
    return render(request, 'listing/listings.html')

def search(request):
    return render(request, 'listing/search.html')
