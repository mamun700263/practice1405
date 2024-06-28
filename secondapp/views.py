from django.shortcuts import render
from .forms import Geeksform

# Create your views here.
def second(request):
    if request.method=='POST':
        form = Geeksform(request.POST)
        if form.is_valid():
            time = form.cleaned_data['How_long_can_You_code']
            print(time)
    else:
        form = Geeksform

    
    
    return render(request,'second.html',{'form':form})