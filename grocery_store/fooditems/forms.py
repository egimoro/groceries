from django.forms import ModelForm
from fooditems.models import FoodItem, Supplier, Location


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['food_type', 'food_price', 'food_description',
                  'other_details', 'date_ordered', 'order_complete',
                  'order_delivered', 'date_delivered'] 


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'supplier_phone', 'supplier_email', 
                  'other_details']


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'zip_postcode', 'country', 'other_details',
                  'suppliers', 'fooditems']