from django.urls import reverse_lazy
from groceries.forms import Grocery_storeForm, GroceriesForm
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, 
                                  DeleteView)

from .models import Grocery_store, Groceries


class Latest_Entry(ListView):
    model = Grocery_store
    template_name = 'groceries/index.html'

    def get_queryset(self):
        return Grocery_store.objects.order_by('-date_established')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 


class Grocery_storeDetailView(DetailView):
    model = Grocery_store
    template_name = 'groceries/grocery_store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  


class GroceriesDetailView(DetailView):
    model = Groceries
    template_name = 'groceries/groceries.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  


class Grocery_storeList(ListView):
    model = Grocery_store
    template_name = 'groceries/grocery_storelist.html'

    def get_queryset(self):
        return Grocery_store.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 


class GroceriesList(ListView):
    model = Groceries
    template_name = 'groceries/grocerieslist.html'

    def get_queryset(self):
        return Groceries.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 


class Grocery_storeCreate(CreateView):
    model = Grocery_store
    form_class = Grocery_storeForm
    template_name = 'groceries/grocery_store_create.html'


class Grocery_storeUpdate(UpdateView):
    model = Grocery_store
    form_class = Grocery_storeForm
    template_name = 'groceries/grocery_store_update.html'


class GroceriesCreate(CreateView):
    model = Groceries
    form_class = GroceriesForm
    template_name = 'groceries/groceries_create.html'


class GroceriesUpdate(UpdateView):
    model = Groceries
    form_class = GroceriesForm
    template_name = 'groceries/groceries_update.html'


class Grocery_storeDelete(DeleteView):
    model = Grocery_store
    template_name = 'groceries/grocery_store_delete.html'

    success_url = reverse_lazy('groceries:grocery_storelist')


class GroceriesDelete(DeleteView):
    model = Groceries
    template_name = 'groceries/groceries_delete.html'
    success_url = reverse_lazy('groceries:grocerieslist')


