from django import forms
from django.forms.widgets import NumberInput
import datetime
from django_countries.fields import  CountryField
from django.core.validators import RegexValidator

best_language =[('c','C'),('c++','C++'),('c#','C#'),('python','PYTHON'),('cobra','COBRA')]
best_language1 =['c','c++','c#']
Year=['2017','2020','2022','2024']
religions=[('islam','ISLAM'),('hindu','HINDU'),('cristian','CRISTIAN')]
gender=[('male','MALE'),('female','FEMALE'),('third','THIRD')]
alphabet_validator = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')

















class ExampleFrom(forms.Form):
    Name = forms.CharField(max_length=50,validators=[alphabet_validator],min_length=5 )



    Fathers_Name = forms.CharField(max_length=50,validators=[alphabet_validator],min_length=5)
    Fathers_NID= forms.IntegerField()
    Fathers_Email=forms.EmailField(required=False)
    Fathers_Nationality = CountryField().formfield()


    Mothers_Name = forms.CharField(max_length=50,validators=[alphabet_validator],min_length=5 )
    Mothers_NID= forms.IntegerField()
    Mothers_Email = forms.EmailField(required=False)
    Mothers_Nationality = CountryField().formfield()

    Date_of_Birth=forms.DateTimeField(widget=NumberInput(attrs={'type':'date'}))
    Religion=forms.ChoiceField(choices=religions)
    Gender = forms.ChoiceField(choices=gender)





    Current_Address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    Current_and_permanent_address_are_same=forms.BooleanField(required=False)
    Permanent_Address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    
    Date_of_Issurance = forms.DateTimeField(initial=datetime.datetime.today)
    Language_choice = forms.ChoiceField(choices=best_language)
    Height = forms.DecimalField()
    Weight = forms.DecimalField()
    Language_Want_to_learn = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=best_language,)
    All_informations_are_authentic=forms.BooleanField(initial=True)
