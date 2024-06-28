from django.shortcuts import render,redirect
from .forms import thirdForm
# Create your views here.
def third(request):
    if request.method=='POST':
        form = thirdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thirdapp')
    else:
        form = thirdForm
    
    return render(request,'third.html',{'form':form})
