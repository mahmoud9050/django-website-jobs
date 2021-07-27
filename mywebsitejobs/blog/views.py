from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
@login_required 
def blog(request):
    
    return render (request,'blog.html')
@login_required 
def single_blog(request):
    


    return render (request,'single-blog.html')

