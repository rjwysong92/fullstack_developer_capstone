# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    description = models.TextField()
    country_of_origin = models.TextField()
    number_of_models = models.IntegerField()

    def __str__(self):
        return self.name
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    CAR_TYPES_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
    ]
    type = models.CharField(max_length=15, 
                            choices=CAR_TYPES_CHOICES, 
                            default='SUV')
    year = models.IntegerField(default=2024,
        validators= [
            MaxValueValidator(2025),
            MinValueValidator(2015)
            ])
    FUEL_TYPE_CHOICES = [
        ('GASOLINE', 'Gasoline'),
        ('HYBRID', 'Hybrid'),
        ('ELECTRIC', 'Electric')]
    efficiency_type = models.CharField(
        max_length=20,
        choices=FUEL_TYPE_CHOICES,
        default='GASOLINE')
    mpg = models.IntegerField(
        blank=True,
        null=False,
        validators=[
            MaxValueValidator(60),
            MinValueValidator(0)
            ])
    mpc = models.IntegerField(
        blank=True,
        null=False,
        validators= [
            MaxValueValidator(500),
            MinValueValidator(0)
            ])
    passenger_capacity = models.IntegerField(default=5,
        validators= [
            MaxValueValidator(15),
            MinValueValidator(2)
            ])
    
    def __str__(self):
        return self.name
