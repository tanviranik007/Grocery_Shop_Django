from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from .models import Carousel,Category,Product,UserProfile
from .models import *


admin.site.register(Carousel)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(Booking)
admin.site.register(Feedback)