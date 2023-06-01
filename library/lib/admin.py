from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}


class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Books, BooksAdmin)
