from django.contrib import admin
from cart.models import *

admin.AdminSite.site_header = '1 admin - 1 project'

from cart.models import *


class CartAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['owner', 'product', 'quantity']})
    ]
    list_display = ['owner', 'product', 'quantity']
    ordering = ['product']
    list_filter = ['quantity']





admin.site.register(Cart, CartAdmin)
admin.site.register(Shipping)
admin.site.register(Payment)
admin.site.register(CreditCard)
admin.site.register(Address)
