from django import forms
from .models import Telefon


class TelefonForm(forms.ModelForm):
    class Meta:
        model = Telefon
        fields = '__all__'

