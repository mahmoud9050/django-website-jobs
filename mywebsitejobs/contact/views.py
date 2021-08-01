from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Contact

# Create your views here.

@login_required 
def contact_us(request):

    contact =Contact.objects.first()



    return render (request,'contact.html',{'contact':contact})

