from django import forms
from .models import Booking


class Dateform(forms.DateInput):
    """This class provides a widget that allows the user to click on it.
    It enhances the user experience when selecting the date for booking.
    """
    input_type = "date"


class Bookingform(forms.ModelForm):
    namn = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "namn"}),
        help_text="*",
        )
    email = forms.EmailField(
        required=True, 
        widget=forms.TextInput(attrs={"placeholder": "namn@exempel.com"}),
        help_text="*",
        )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "+46701234567"}),
        help_text="This field is optional.",
        )

    class Meta:
        model = Booking
        exclude = ("user",)
        widgets = {
            "date": Dateform()
        }