from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pymongo import MongoClient
# Create your views here.

class InsightsAPI(APIView):
    def get(self, request):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["dashboard_db"]
        insights = list(db.insights.find({}, {'_id': 0}))
        return Response(insights)
    

def dashboard_view(request):
    return render(request, "dashboard.html")
