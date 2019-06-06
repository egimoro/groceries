from django.http import HttpResponseRedirect
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
    template_name = 'groceries/grocery_storeList.html'

    def get_queryset(self):
        return Grocery_store.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 


class GroceriesList(ListView):
    model = Groceries
    template_name = 'groceries/groceriesList.html'

    def get_queryset(self):
        return GroceriesList.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 

