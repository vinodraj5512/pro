from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>hi all e careful!!!!</h1>")
def func(request):
    return render(request,'sample.html')
