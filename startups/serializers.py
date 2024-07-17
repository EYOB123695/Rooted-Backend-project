from rest_framework import serializers
from .models import Startup

class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ['name', 'location', 'year_founded', 'industry']  # Updated to match the Startup model fields
