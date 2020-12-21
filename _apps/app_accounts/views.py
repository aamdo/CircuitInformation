from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounts/home.html',context)

def about(request):
    context = {}
    return HttpResponse('<h2>' + 'نظام معلومات الدوائر بمنطقة القصيم' + '</h2>')
 

