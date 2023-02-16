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
    path('registration/', registration, name="registration"),
    path('userlogin/', userlogin, name="userlogin"),
    path('profile/', profile, name="profile"),
    path('logout/', logoutuser, name="logout"),
    path('change-password/', change_password, name="change-password"),
    path('user-product/<int:pid>/', user_product, name="user_product"),
    path('product-detail/<int:pid>/', product_detail, name="product_detail"),
    
    path('add-to-cart/<int:pid>/', addToCart, name="addToCart"),
    path('cart/', cart, name="cart"),
    path('incredecre/<int:pid>/', incredecre, name="incredecre"),
    path('deletecart/<int:pid>/', deletecart, name="deletecart"),
    path('booking/', booking, name="booking"),
    path('my-order/', myOrder, name="myorder"),
    path('user-order-track/<int:pid>/', user_order_track, name="user_order_track"),
    path('change-order-status/<int:pid>/', change_order_status, name="change_order_status"),
    path('user-feedback/', user_feedback, name="user_feedback"),
    path('manage-feedback/', manage_feedback, name="manage_feedback"),
    path('delete-feedback/<int:pid>/', delete_feedback, name="delete-feedback"),
    path('feedback-read/<int:pid>/', read_feedback, name="read_feedback"),
    path('payment/', payment, name="payment"),
    path('manage-order/', manage_order, name="manage_order"),
    path('delete-order/<int:pid>/', delete_order, name="delete-order"),   

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)