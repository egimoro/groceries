from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView,
                                  DeleteView, UpdateView)
from fooditems.forms import SupplierForm, LocationForm, FoodItemForm                                 
from .models import Supplier, Location, FoodItem
from groceries.models import Groceries


class Latest_Fooditem(ListView):
    model = FoodItem
    template_name = 'fooditems/home.html'
    
    def get_queryset(self):
        return FoodItem.objects.order_by('-date_ordered')[:7]


class FoodItemList(ListView):
    model = FoodItem
    template_name = 'fooditems/fooditems_list.html'

    def get_queryset(self):
        return FoodItem.objects.all()


class GroceriesView(ListView):
    model = Groceries
    template_name = 'groceries/index.html'

    def get_queryset(self):
        return Groceries.objects.all()


class FoodItemDetails(DetailView):
    model = FoodItem
    template_name = 'fooditems/fooditems.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FoodItemCreate(CreateView):
    model = FoodItem
    form_class = FoodItemForm
    template_name = 'fooditems/add_fooditem.html'


class FoodItemEdit(UpdateView):
    model = FoodItem
    form_class = FoodItemForm
    template_name = 'fooditems/update_fooditem.html'


class FoodItemDelete(DeleteView):
    model = FoodItem
    template_name = 'fooditems/delete_fooditem.html'
    success_url = reverse_lazy('fooditems:fooditems_list')


class SupplierList(ListView):
    model = Supplier
    template_name = 'fooditems/suppliers_list.html'

    def get_queryset(self):
        return Supplier.objects.all()


class SupplierDetail(DetailView):
    model = Supplier
    template_name = 'fooditems/suppliers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SupplierAdd(CreateView): 
    model = Supplier
    form_class = SupplierForm
    template_name = 'fooditems/add_supplier.html'


class SupplierUpdate(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'fooditems/update_supplier.html'
   

class SupplierDelete(DeleteView):
    model = Supplier
    template_name = 'fooditems/delete_supplier.html'
    success_url = reverse_lazy('fooditems:suppliers_list')


class LocationList(ListView):
    model = Location
    template_name = 'fooditems/locations_list.html'

    def get_queryset(self):
        return Location.objects.all() 


class LocationDetails(DetailView):
    model = Location
    template_name = 'fooditems/locations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LocationCreate(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'fooditems/add_location.html'


class LocationUpdate(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'fooditems/update_location.html'


class LocationDelete(DeleteView):
    model = Location
    template_name = 'fooditems/delete_location.html'
    success_url = reverse_lazy('fooditems:locations_list')





    
  