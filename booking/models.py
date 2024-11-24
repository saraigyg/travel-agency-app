from django.db import models
from django.contrib.auth.models import User
from tours.models import Tour

#Create database for authentification and booking details
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField()
    number_of_people = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.tour.title}"

