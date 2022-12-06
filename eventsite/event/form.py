from django import forms
from django.forms import ModelForm
from .models import Venue

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'address', 'zip_code', 'phone', 'website', 'email_address']