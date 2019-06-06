from django.urls import path

from groceries.views import (Latest_Entry, Grocery_storeDetailView,
                             GroceriesDetailView, Grocery_storeList)

app_name = 'groceries'

urlpatterns = [
    path('', Latest_Entry.as_view(), name='index'),
    path('<int:pk>/grocery_store', Grocery_storeDetailView.as_view(),
         name='grocery_store'),
    path('<int:pk>/groceries/', GroceriesDetailView.as_view(),
         name='groceries'),
    path('grocery_storeList/', Grocery_storeList.as_view(),
         name='grocery_storeList'),
  
     
]  