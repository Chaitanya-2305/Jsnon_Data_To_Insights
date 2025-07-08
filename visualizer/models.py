from django.db import models

# Create your models here.

class Insight(models.Model):
    intensity = models.IntegerField(null=True, blank=True)
    likelihood = models.IntegerField(null=True, blank=True)
    relevance = models.IntegerField(null=True, blank=True)
    start_year = models.CharField(max_length=10, blank=True, null=True)
    end_year = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    topic = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    pestle = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    swot = models.CharField(max_length=100, blank=True, null=True)
    title = models.TextField()
    insight = models.TextField()
    url = models.URLField()
