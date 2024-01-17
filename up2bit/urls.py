from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views


#from userextend.forms import AuthenticationNewForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('coin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
