from django.contrib import admin

from .models import Item, Order, Discount, Tax


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'description', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', )


class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'tax')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tax, TaxAdmin)
