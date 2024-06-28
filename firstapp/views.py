from django.shortcuts import render
from .forms import ExampleFrom 
def home(request):

        form = ExampleFrom
        
        return render(request, 'firstapp.html', {'form': form})

def homepage(request):
        return render(request, 'homepage.html')

