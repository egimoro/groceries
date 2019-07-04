from django.db import models
from django.utils import timezone
from django.urls import reverse


class Supplier(models.Model):
    __tablename__ = 'supplier'

    supplier_name = models.CharField(max_length=200)
    supplier_phone = models.CharField(max_length=20)
    supplier_email = models.CharField(max_length=50)
    other_details = models.CharField(max_length=350)

    def __str__(self):
        return self.supplier_name


class FoodItem(models.Model):
    __tablename__ = 'fooditem'

    MEAT = 'ME'
    FISH = 'FH'
    FRUITS = 'FT'
    VEGETABLES = 'VG'
    MUSHROOMS = 'MH'
    FOOD_CHOICE = [
        (MEAT, 'meat'),
        (FISH, 'fish'),
        (FRUITS, 'fruits'),
        (MUSHROOMS, 'mushrooms'),
    ]
    food_type = models.CharField(max_length=2, choices=FOOD_CHOICE, 
                                 default=MEAT,)
    food_price = models.FloatField()
    food_description = models.CharField(max_length=200)
    other_details = models.CharField(max_length=350)
    locations = models.ManyToManyField(Supplier, through='Location')
    date_ordered = models.DateTimeField('Date Ordered',
                                        default=timezone.now(), null=True,
                                        blank=True)
    order_complete = models.BooleanField(default=True)
    order_delivered = models.BooleanField(default=True)
    date_delivered = models.DateTimeField('Date Delivered',
                                          default=timezone.now(), null=True,
                                          blank=True)

    def __str__(self):
        return self.food_type
    
    def get_absolute_url(self):
        return reverse('fooditems:fooditems', kwargs={'pk': self.pk})
        

class Location(models.Model):
    __tablename__ = 'location'
    
    city = models.CharField(max_length=150)
    zip_postcode = models.CharField(max_length=15)
    country = models.CharField(max_length=150)
    other_details = models.CharField(max_length=350)
    suppliers = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    fooditems = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    
