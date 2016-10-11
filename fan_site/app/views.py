from django.shortcuts import render
from app.models import Region, House, SmallHouse
# Create your views here.

def home_view(request):
    return render(request, "home.html")

def bio_view(request):
    context = {
    "connor" : House.objects.filter(name="Redmond")
    }
    return render(request, "bio.html", context)

def detail_view(request):
    context = {
    "regions" : Region.objects.all()
    }
    return render(request, "detail.html", context)

def region_view(request, region_id):
    context = {
    "region" : Region.objects.get(id=region_id),
    "houses" : SmallHouse.objects.filter(region = region_id)

    }
    return render(request, "region.html", context)
