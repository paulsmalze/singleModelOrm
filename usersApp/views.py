from django.shortcuts import render
#import the class from models
from .models import User

# Create your views here.
#show all the data from the table

def index(request):
    context = {
        "all_users" : User.objects.all().values()
    }
    
    return render(request, 'index.html',context)