from django.db import models

# Booking Table
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
# Menu Table
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} -price: {str(self.price)}'