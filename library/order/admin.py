from order.models import Order
from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'created_at', 'end_at', 'plated_end_at')
    list_filter = ('id', 'book')
    fieldsets = (
        ('Chose a user and a book', {
            'fields': (('user', 'book'),)
        }),
        ('Chose the date', {
            'fields': (('end_at', 'plated_end_at'),),
        }),
    )


admin.site.register(Order, OrderAdmin)
