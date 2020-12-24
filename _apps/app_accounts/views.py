from django.shortcuts import render
from .models import LogIn
from .forms import LoginForm


# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounts/home.html',context)

def about(request):
    dataform = LoginForm(request.POST)
    if request.method == 'POST':
        if dataform.is_valid:
                dataform.save()
 

    
    context = {'lf':LoginForm}
    return render(request,'accounts/about.html',context)
 

