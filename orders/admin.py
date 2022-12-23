from django.contrib import admin

# Register your models here.
from .models import Orders,Recipt
admin.site.register(Orders)
admin.site.register(Recipt)
