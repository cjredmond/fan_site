from django.shortcuts import render
from app.models import Region, House
# Create your views here.

def home_view(request):
    return render(request, "home.html")

def bio_view(request):
    return render(request, "bio.html")

def detail_view(request):
    context = {
    "regions" : Region.objects.all()
    }
    return render(request, "detail.html", context)
