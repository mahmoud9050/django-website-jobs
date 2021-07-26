from django.urls import reverse
from django.shortcuts import redirect, render
from . models import Jobs
from django.core.paginator import Paginator
from .form import JobsFormes , ApplyForm
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


def jobs (request):
    job_list =Jobs.objects.all()
    paginator = Paginator(job_list, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)





    context ={
        'alljobs':page_obj
        }

    return render (request,'jobs.html',context)
    
def job_details (request,slug):
    job_id = Jobs.objects.get(slug=slug)

    if request.method== 'POST':
        form=ApplyForm(request.POST ,request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.job_name=job_id
            myform.save()
            return redirect(reverse('jobs:jobs' ))
            
    
    else:
        form = ApplyForm()
    
    context ={ 'singeljob':job_id ,'form':form  }

    return render (request ,'job_details.html',context )


def post_jop (request):

    if request.method == 'POST':
        form = JobsFormes(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=True)
            myform.save()
            return redirect(reverse('jobs:jobs' ))

    else:
        form = JobsFormes ()
    return render (request , 'post-jop.html',{'form':form})
   

