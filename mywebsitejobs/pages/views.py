from django.shortcuts import render

# Create your views here.
def index (request):
    return render (request ,'pages/index.html')

def candidate (request):
    return render (request ,'pages/candidate.html')

def blog (request):
    return render (request , 'pages/blog.html')

def jobs (request):
    return render (request , 'pages/jobs.html')
    
def job_details (request):
    return render (request , 'pages/job_details.html')

def contact (request):
    return render (request , 'pages/contact.html')

def single_blog (request):
    return render (request , 'pages/single-blog.html')


def elements (request):
    return render (request , 'pages/elements.html')


def post_jop (request):
    return render (request , 'pages/post-jop.html')

def login (request):
    return render (request , 'pages/login.html')

