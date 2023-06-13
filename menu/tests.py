from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from .models import Booking

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
        field_label = booking._meta.get_field('email')
        self.assertEquals(field_label, 'email')

    def test_phone_label(self):
        bookig = Booking.objects.get(id=1)
        field_label = booking._meta.get_field('phone')
        self.assertEquals(field_label, 'phone')

