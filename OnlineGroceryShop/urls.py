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
    path('view-category/', view_category, name="view-category"),
    path('edit-category/<int:pid>/', edit_category, name="edit-category"),
    path('delete-category/<int:pid>/', delete_category, name="delete-category"),
    path('add-product/', add_product, name='add-product'),
    path('view-product/', view_product, name='view-product'),
    path('edit-product/<int:pid>/', edit_product, name="edit_product"),
    path('delete-product/<int:pid>/', delete_product, name="delete_product"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)