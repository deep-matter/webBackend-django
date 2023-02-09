from django.shortcuts import render
from listing.models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage  

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    last_list = {
     "last_list": listings
    }
    return render(request, 'pages/index.html', last_list)


def about(request):
    realtors_list = Realtor.objects.all()[:3]
    is_Mvp = Realtor.objects.order_by('-hire_date').filter(is_mvp=True)

    dict_realtors = {
        "Realtors" : realtors_list,
        "is_mvp" : is_Mvp
     }
    return render(request, 'pages/about.html',dict_realtors)


# def listing(request):

#     return render(request, 'listing/listing.html')
 
    # paginator = Paginator(listings, 6)
    # page_name = request.GET.get('page')
    #page_number = paginator.get_page(page_name)

