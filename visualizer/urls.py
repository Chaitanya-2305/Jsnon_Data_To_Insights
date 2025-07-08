from django.urls import path
from .views import InsightsAPI
from .views import dashboard_view

urlpatterns = [
    path('', dashboard_view),
    path('api/insights/', InsightsAPI.as_view()),
]

