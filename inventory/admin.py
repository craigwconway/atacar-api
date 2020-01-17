from django.contrib import admin

from inventory.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'make', 'model',
                    'price', 'created', 'updated')


admin.site.register(Car, CarAdmin)
