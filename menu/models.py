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
    ('6', '6'),
)

# options for the time of the booking

TIMES = (
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
)


class Booking(models.Model):
    class Meta:
        unique_together = ('date', 'time', 'guests')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_booking')
    namn = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=24, blank=True, null=True)
    guests = models.CharField(max_length=2, choices=GEUST, default='2')
    time = models.CharField(max_length=30, choices=TIMES, default='10:00')
    date = models.DateField()

    def __str__(self):
        return self.namn






    

