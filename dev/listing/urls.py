from django.urls import path , include
from . import views 

urlpatterns = [
    path('', views.listing, name='listing'),
    path('<int:listing_id>', views.listings, name='listings'),
    path('search/', views.search, name='search')
 ]