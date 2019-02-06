from django.contrib import admin
from .models import Shoptext
# Register your models here.

@admin.register(Shoptext)
class Shoptext(admin.ModelAdmin):
    pass