from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=50, default='Unknown')  # default value

    def __str__(self):
        return self.name

class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    duration = models.IntegerField()  # Duration in days

    def __str__(self):
        return self.title

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    special_requests = models.TextField(blank=True, null=True)  
    email = models.EmailField()
    phone = models.CharField(max_length=15) 

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.tour.title}"


