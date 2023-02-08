from django.shortcuts import render
from .models import Listing

def listing(request):
    listings = Listing.objects.all()
    content = {
        "listing": listings,
    }
    return render(request, 'listing/listing.html',content)

def listings(request,listing_id):
    return render(request, 'listing/listings.html')

def search(request):
    return render(request, 'listing/search.html')
