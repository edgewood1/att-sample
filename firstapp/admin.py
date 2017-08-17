from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'home']



admin.site.register(Item, ItemAdmin)
