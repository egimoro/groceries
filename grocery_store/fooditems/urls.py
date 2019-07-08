from django.urls import path
from fooditems.views import (Latest_Fooditem, GroceriesView, FoodItemList,
                             FoodItemDetails, FoodItemCreate, FoodItemEdit,
                             FoodItemDelete, SupplierList,
                             SupplierDetail, LocationList, LocationDetails,
                             SupplierAdd, SupplierUpdate, SupplierDelete,
                             LocationCreate, LocationUpdate, LocationDelete)
app_name = 'fooditems'
urlpatterns = [
    path('fooditems/', Latest_Fooditem.as_view(), name='home'),

    path('fooditems_list/', FoodItemList.as_view(), name='fooditems_list'),

    path('groceries/groceries_list/', GroceriesView.as_view(), 
         name='groceries'),

    path('<int:pk>/fooditems/', FoodItemDetails.as_view(),
         name='fooditems'),

    path('add_fooditem/', FoodItemCreate.as_view(), name='add_fooditem'),
    path('<int:pk>/update_fooditem/', FoodItemEdit.as_view(), 
         name='update_fooditem'),

    path('<int:pk>/delete_fooditem/', FoodItemDelete.as_view(),
         name='delete_fooditem'),

    path('suppliers_list/', SupplierList.as_view(), name='suppliers_list'),

    path('<int:pk>/suppliers/', SupplierDetail.as_view(), name='suppliers'),

    path('locations_list/', LocationList.as_view(), name='locations_list'),

    path('<int:pk>/locations/', LocationDetails.as_view(), name='locations'),

    path('add_supplier/', SupplierAdd.as_view(), name='add_supplier'),

    path('<int:pk>/update_supplier/', SupplierUpdate.as_view(), name='update_supplier'),

    path('<int:pk>/delete_supplier/', SupplierDelete.as_view(), name='delete_supplier'),

    path('add_location/', LocationCreate.as_view(), name='add_location'),

    path('<int:pk>/update_location', LocationUpdate.as_view(), name='update_location'),

    path('<int:pk>/delete_location', LocationDelete.as_view(), name='delete_location'),
   
]