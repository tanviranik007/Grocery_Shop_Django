from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Carousel,Category


admin.site.register(Carousel)
admin.site.register(Category)