from django.contrib import admin
from .models import Groceries, Grocery_store


class Grocery_StoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['store_name', 'owner', 'location']}),
        ('Date information', {'fields': ['date_established']}),
    ]


admin.site.register(Groceries)
admin.site.register(Grocery_store, Grocery_StoreAdmin)