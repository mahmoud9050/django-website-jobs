from django.shortcuts import render
from . models import Jobs
from django.core.paginator import Paginator
from .form import JobsFormes

# Create your views here.
def index (request):
    return render (request ,'pages/index.html')

def candidate (request):
    return render (request ,'pages/candidate.html')

def blog (request):
    
    return render (request , 'pages/blog.html')

def jobs (request):
    job_list =Jobs.objects.all()
    paginator = Paginator(job_list, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)





    context ={
        'alljobs':page_obj
        }

    return render (request,'pages/jobs.html',context)
    
def job_details (request,slug):
    job_id = Jobs.objects.get(slug=slug)
    
    context ={
    'singeljob':job_id
    }

    return render (request , 'pages/job_details.html',context)

def contact (request):
    return render (request , 'pages/contact.html')

def single_blog (request):
    return render (request , 'pages/single-blog.html')


def elements (request):
    return render (request , 'pages/elements.html')


def post_jop (request):

    if request.method == 'POST':
        pass

    else:
        form = JobsFormes ()
    return render (request , 'pages/post-jop.html',{'form':form})
   

def login (request):
    return render (request , 'pages/login.html')

