from django.contrib import admin

from orders.models import Order, Stock, ProductStock


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'created_at',)


class StockProductInline(admin.TabularInline):
    model = ProductStock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'created_at',)
    inlines = [StockProductInline]
