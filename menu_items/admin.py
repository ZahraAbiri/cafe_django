from django.contrib import admin

# Register your models here.
from .models import Menu_item,Categories
admin.site.register(Menu_item)
admin.site.register(Categories)
