from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active", "pre_order", "valid_from", "valid_until")
    list_filter = ("is_active",)
    readonly_fields = ('created_by', 'updated_by',)
    list_editable = ("name", "is_active", "pre_order",)


admin.site.register(Product, ProductAdmin)
