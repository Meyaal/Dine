from django import forms
from .models import Booking
from django.utils import timezone
from django.core.exceptions import ValidationError


class Dateform(forms.DateInput):
    """This class provides a widget that allows the user to click on it.
    It enhances the user experience when selecting the date for booking.
    """
    input_type = "date"


class Bookingform(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "name"}),
        help_text="*",
        )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "name@exemple.com"}),
        help_text="*",
        )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "+46701234567"}),
        help_text="This field is optional.",
        )
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.localdate():
            raise ValidationError('You can not make a bookin for passed date!')
        return date

    class Meta:
        model = Booking
        exclude = ("user",)
        widgets = {
            "date": Dateform()
        }
