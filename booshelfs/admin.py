from django.contrib import admin

# Register your models here.
from .models import Author, Book, Language
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Book)
