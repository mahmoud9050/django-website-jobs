from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from all_jobs.models import Jobs

# Create your views here.
def home(request):
    all_jobs =Jobs.objects.all()


    context ={'all_jobs':all_jobs}

    


    return render (request,'home.html',context)

