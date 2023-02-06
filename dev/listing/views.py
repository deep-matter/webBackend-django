from django.shortcuts import render

def listing(request):
    return render(request, 'listing/listing.html')

def listings(request):
    return render(request, 'listing/listings.html')

def search(request):
    return render(request, 'listing/search.html')
