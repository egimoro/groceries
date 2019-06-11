from django.test import TestCase
import datetime
from .models import Groceries, Grocery_store
from django.utils import timezone


class Grocery_storeModelTests(TestCase):
    def recent_establishment_in_future_date_test(self):
        time = timezone.now()+datetime.timedelta(days=30)
        future_date = Grocery_store(date_established=time)
        self.assertIs(future_date.was_established_recently(), False) 


class GroceriesModelTests(TestCase):
    def recent_ordered_in_future_date_test(self):
        time = timezone.now()+datetime.timedelta(days=30)
        future_date = Groceries(date_ordered=time)
        self.assertIs(future_date.was_ordered_recently(), False) 