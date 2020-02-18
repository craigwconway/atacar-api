from django.contrib import admin

from inventory.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'make', 'model',
                    'price', 'created', 'updated')


admin.site.register(Item, ItemAdmin)
