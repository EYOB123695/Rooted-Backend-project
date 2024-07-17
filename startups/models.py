from django.db import models
class Startup(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.name

