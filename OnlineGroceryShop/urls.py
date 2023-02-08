from django.contrib import admin
from django.urls import path
from groceryapp.views import *
from django.conf import settings
from django.conf.urls.static import static
   
from groceryapp.views import home, index, about,main,adminLogin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('index/', index, name="index"),
    path('about/', about, name="about"),
    path('main/', main, name="main"),
    path('admin-login/', adminLogin, name="admin-login"),
    path('adminhome/', adminHome, name="adminhome"), 
    path('admindashboard/', admin_dashboard, name="admindashboard"),
    path('add-category/', add_category, name="add-category"), 
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)