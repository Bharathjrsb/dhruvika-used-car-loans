from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ads import views as ads_views

urlpatterns = [
    path('', ads_views.home, name='home'),
    path('ads/', ads_views.gallery, name='gallery'),
    path('ad/<int:pk>/', ads_views.ad_detail, name='ad_detail'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

