from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime


class Grocery_store(models.Model):
    __tablename__ = 'grocery_store'

    store_name = models.CharField(max_length=200, default=None)
    owner = models.CharField(max_length=150, default=None)
    location = models.CharField(max_length=200, default=None)
    date_established = models.DateField('date established')

    def __str__(self):
        return self.store_name
    
    def get_absolute_url(self):
        return reverse('groceries:grocery_store', kwargs={'pk': self.pk}) 
    
    def was_estblished_recently(self):
        now = timezone.now()

        return now - datetime.timedelta(days=1) <= self.pub_date <= now
     
    was_estblished_recently.admin_order_field = 'date_established'

    was_estblished_recently.boolean = True

    was_estblished_recently.short_description = 'Established recently?'

       
class Groceries(models.Model):
    __tablename__ = 'groceries' 

    food = 'fo'
    drinks = 'dr'
    other_items = 'ot'
    Item_choices = [
        (food, 'food'),
        (drinks, 'drinks'),
        (other_items, 'other items'),

    ]
    grocery_type = models.CharField(max_length=2,
                                    choices=Item_choices,
                                    default=food,
                                    )
    brand = models.CharField(max_length=150)
    quantity = models.IntegerField(default=None)
    price = models.FloatField(default=None)
    date_ordered = models.DateField('date ordered')
    is_available = models.BooleanField(default=True)
    grocery = models.ForeignKey(Grocery_store, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand
        
    def get_absolute_url(self):
        return reverse('groceries:groceries', kwargs={'pk': self.pk}) 
    
    def was_ordered_recently(self):
        now = timezone.now()

        return now - datetime.timedelta(days=1) <= self.pub_date <= now
     
    was_ordered_recently.admin_order_field = 'date_ordered'

    was_ordered_recently.boolean = True

    was_ordered_recently.short_description = 'Ordered recently?'

