from django.db import models


class Grocery_store(models.Model):
    __tablename__ = 'grocery_store'

    store_name = models.CharField(max_length=200, default=None)
    owner = models.CharField(max_length=150, default=None)
    location = models.CharField(max_length=200, default=None)
    date_established = models.DateField('date established')

    def __str__(self):
        return self.store_name

        
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