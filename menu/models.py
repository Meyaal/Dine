from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# options for how many guests in the booking
GEUST = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

# options for the time of the booking

TIMES = (
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
)


class Booking(models.Model):
    class Meta:
        unique_together = ('date', 'time', 'guests')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_booking')
    namn = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.IntegerField(blank=True, null=True)
    guests = models.CharField(max_length=2, choices=GEUST, default='2')
    time = models.CharField(max_length=30, choices=TIMES, default='10:00')
    date = models.DateField()
    def __str__(self):
        return self.namn







    

