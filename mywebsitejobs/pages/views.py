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
    context ={
        'alljobs':job_list
        }

    return render (request,'pages/jobs.html',context)
    
def job_details (request,id):
    job_id = Jobs.objects.get(id=id)
    
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

