from django.contrib import admin

from .models import Category, Product, Tag


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'description')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)