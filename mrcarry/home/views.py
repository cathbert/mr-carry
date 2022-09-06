from django.shortcuts import render
from .models import Load
# Create your views here.

def home_view(request):
    print(Load.objects.filter(customer=request.user))
    return render(request, 'home/index.html')