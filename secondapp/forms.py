from django import forms
from django.forms.widgets import NumberInput
import datetime

cp_language=[('c++','CPP'),('java','JAVA'),('py','PYTHON')]


class Geeksform(forms.Form):
    First_Name = forms.CharField(max_length=50,min_length=10,help_text='Enter your first name')
    Last_Name = forms.CharField(max_length=50,min_length=10,help_text='Enter your Last name')
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput())
    You_can_code = forms.BooleanField()
    Language_you_use_for_cp = forms.ChoiceField(choices=cp_language)
    You_want_to_join_on = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    CGPA = forms.DecimalField()
    How_long_can_You_code = forms.DurationField(help_text='hello it is HH:MM:SS')
    Your_mark_sheet=forms.FileField()
    YOur_formal_photo_plz = forms.ImageField()
    Student_now = forms.NullBooleanField()
    linkedin = forms.URLField()
    




