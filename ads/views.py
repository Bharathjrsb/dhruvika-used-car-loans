from django.shortcuts import render, get_object_or_404
from .models import Ad

def home(request):
    return render(request, "ads/home.html")

def gallery(request):
    ads = Ad.objects.filter(is_active=True)
    return render(request, 'ads/gallery.html', {'ads': ads})

def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk, is_active=True)
    return render(request, 'ads/ad_detail.html', {'ad': ad})
