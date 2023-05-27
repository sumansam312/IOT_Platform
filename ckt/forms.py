from django import forms
from .models import CircuitModel

class CircuitForm(forms.ModelForm):
    class Meta:
        model = CircuitModel
        fields = ['led_1','led_2' ]