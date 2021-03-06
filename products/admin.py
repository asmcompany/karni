from django.contrib import admin

from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
