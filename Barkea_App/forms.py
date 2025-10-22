from django import forms
from .models import Contact
from .models import Reservation

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation 
        fields =  ['name', 'email', 'phone', 'date', 'comment']      
        
       