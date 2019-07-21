from django.urls import path

from groceries.views import (Latest_Entry, Grocery_storeDetailView,
                             GroceriesDetailView, Grocery_storeList, 
                             GroceriesList, Grocery_storeCreate,
                             Grocery_storeUpdate, GroceriesCreate,
                             GroceriesUpdate, Grocery_storeDelete,
                             GroceriesDelete, FoodItemView)


app_name = 'groceries'

urlpatterns = [
    path('groceries/', Latest_Entry.as_view(), name='home'),
    path('<int:pk>/grocery_store/', Grocery_storeDetailView.as_view(),
         name='grocery_store'),

    path('<int:pk>/groceries/', GroceriesDetailView.as_view(),
         name='groceries'),

    path('grocery_store_list/', Grocery_storeList.as_view(),
         name='grocery_store_list'),

    path('groceries_list/', GroceriesList.as_view(),
         name='groceries_list'), 
    path('grocery_store_create/', Grocery_storeCreate.as_view(),
         name='grocery_store_create'),

    path('<int:pk>/grocery_store_update/', Grocery_storeUpdate.as_view(),
         name='grocery_store_update'),

    path('groceries_create/', GroceriesCreate.as_view(),
         name='groceries_create'),

    path('<int:pk>/groceries_update/', GroceriesUpdate.as_view(),
         name='groceries_update'),

    path('<int:pk>/grocery_store_delete/', Grocery_storeDelete.as_view(),
         name='grocery_store_delete'),
    
    path('<int:pk>/groceries_delete/', GroceriesDelete.as_view(),
         name='groceries_delete'),
    path('fooditems/fooditems_list/', FoodItemView.as_view(), 
         name='fooditems'),

     
]  
