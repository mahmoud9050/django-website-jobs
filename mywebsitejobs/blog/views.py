from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Blog

# Create your views here.
from django.shortcuts import render

# Create your views here.
@login_required 
def blog(request):
    
    allblogs = Blog.objects.all()

    context ={'allblogs':allblogs}

    return render (request,'blog.html',context)
@login_required 
def single_blog(request,slug):
    blog = Blog.objects.get(slug=slug)

    

    context ={'blog':blog}
    


    return render (request,'single-blog.html',context)

