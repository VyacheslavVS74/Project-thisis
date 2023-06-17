from django.contrib import admin

from django.contrib import admin
from .models import Order, StatusCrm


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_works', 'order_name', 'order_phone', 'order_status', 'order_dt')
    list_display_links = ('id', 'order_works')
    search_fields = ('id', 'order_works', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')



admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)