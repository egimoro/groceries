from django.urls import path
from .views import SignUpView, Grocery_StoreView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('groceries/home', Grocery_StoreView.as_view(), name='home'),

]
