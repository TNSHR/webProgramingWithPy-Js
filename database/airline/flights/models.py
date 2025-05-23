from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="departures")   # Departure city        
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="arrivals")   # Arrival city
    duration = models.IntegerField()   # Duration in minutes
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
class Passenger(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")   # Many-to-many relationship with Flight

    def __str__(self):
        return f"{self.first} {self.last}"