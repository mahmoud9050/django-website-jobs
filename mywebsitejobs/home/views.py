from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from all_jobs.models import Jobs
from accounts.models import Profile

# Create your views here.
def home(request):
    all =Profile.objects.get(user=request.user)
    all_jobs =Jobs.objects.all()
    paginator = Paginator(all_jobs, 5) # Show 3 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

   


    context ={'paginator':page_obj ,'all':all ,'all_jobs':all_jobs}

    return render (request,'home.html',context  )

