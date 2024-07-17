from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Startup
from .serializers import StartupSerializer

# View for the home page
def home(request):
    return render(request, 'startups/home.html')

# API endpoint for searching startups
@api_view(['GET'])
def search_startups(request):
    query = request.GET.get('query', '')  # Get the search query from the GET request
    startups = Startup.objects.filter(name__icontains=query)  # Filter startups by name
    serializer = StartupSerializer(startups, many=True)  # Serialize the data
    return Response(serializer.data)  # Return the data as JSON
