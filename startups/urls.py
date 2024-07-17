from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL for the home page
    path('api/search/', views.search_startups, name='search_startups_api'),  # API endpoint for searching startups
]
