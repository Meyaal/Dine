from django import forms
from .models import Booking

class Dateform(forms.DateInput):
    input_type = "date"

class Bookingform(forms.ModelForm):
    namn = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "namn"})
        )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "namn@exempel.com"})
        )
    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={"placeholder": "+ 123456789"}), 
        required=False
        )
    class Meta:
        model = Booking
        exclude = ("user",)
        widgets = {
            "date": Dateform()
        }