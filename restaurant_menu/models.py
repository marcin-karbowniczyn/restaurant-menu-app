from django.db import models
from django.contrib.auth.models import User

# If author is deleted, models.CASCADE will delete all the meals that this author had created.
# models.PROTECT -> I won't be able to delete a User.
# models.SET_NULL -> The user will be deleted, and it will be set to NULL on the item instances.


MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts')
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available'),
)


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)  # auto_now_add -> Automatically set the field to now when the object is first created.
    date_updated = models.DateTimeField(auto_now=True)  # auto_now -> Automatically set the field to now every time the object is saved.

    def __str__(self):
        return self.meal
