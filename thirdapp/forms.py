# myapp/forms.py
from django import forms
from .models import Mymodel

class thirdForm(forms.ModelForm):
    class Meta:
        model = Mymodel
        fields = '__all__'
