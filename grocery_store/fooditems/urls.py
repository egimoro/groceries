from django.urls import path
from fooditems.views import (Latest_Fooditem, GroceriesView, FoodItemList,
                             FoodItemDetails, FoodItemCreate, FoodItemEdit,
                             FoodItemDelete, SupplierList, LocationList,
                             SupplierDetail, LocationDetail)
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
    path('suppliers_list', LocationList.as_view(), name='suppliers_list'),
    path('<int:pk>/suppliers', SupplierDetail.as_view(), name='suppliers'),
    path('<int:pk>/suppliers', LocationDetail.as_view(), name='suppliers'),
]