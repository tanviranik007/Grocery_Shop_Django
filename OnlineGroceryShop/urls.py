from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from groceryapp.views import home, index, about,main
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('index/', index, name="index"),
    path('about/', about, name="about"),
    path('main/', main, name="main"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)