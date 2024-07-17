from django.contrib import admin
from django.urls import path, include  # Import `include` to include app-specific URLs

urlpatterns = [
    path('', include('startups.urls')),  # Include URLs from the startups app for the root path
    path('admin/', admin.site.urls),  # Admin interface URL
]
