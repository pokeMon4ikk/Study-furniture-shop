from django.contrib import admin
from mainapp.models import ProductsItem, Products

# Register your models here.
admin.site.register(ProductsItem)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    list_editable = ('price', 'quantity')
