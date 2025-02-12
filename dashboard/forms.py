from django import forms
from .models import FakultetData


class FakultetDataForm(forms.ModelForm):
    class Meta:
        model = FakultetData
        fields = '__all__'