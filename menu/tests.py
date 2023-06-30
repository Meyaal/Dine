from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from .models import Booking
from django.db import DataError

# Create your tests here.

class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='john doe', password='12345')
        Booking.objects.create(
            user=user, namn='test booking', email='email@.com', 
            phone='+ 123456789', guests='4', time='10:00', date=date.today())

    def test_name_label(self):
        booking = Booking.objects.get(id=1)
        field_label = booking._meta.get_field('namn').verbose_name
        self.assertEquals(field_label, 'namn')

    def test_email_label(self):
        booking = Booking.objects.get(id=1)
        field_label = booking._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_name_length(self):
        user = User.objects.create_user(username='test user', password='12345')
        namn = 'h' * 1024
        email = 'test@test'
        guests = '2'
        time = '10:00'
        date = '1970-01-01'
        with self.assertRaises(DataError):
            booking = Booking.objects.create(
                user=user, namn=namn, email=email, guests=guests, 
                time=time, date=date)
            booking.check
            booking.save()