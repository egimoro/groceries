from django.forms import ModelForm
from groceries.models import Groceries, Grocery_store


class Grocery_storeForm(ModelForm):
    class Meta:
        model = Grocery_store
        fields = ['store_name', 'owner', 'location', 'date_established']


class GroceriesForm(ModelForm):
    class Meta:
        model = Groceries
        fields = ['grocery_type', 'brand', 'quantity', 'price', 'date_ordered', 'is_available', 'grocery']