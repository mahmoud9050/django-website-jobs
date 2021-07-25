from django.urls import path
from  . import views



urlpatterns = [
    path ('' , views.index , name = 'index'),
    path ('index' , views.index , name = 'index'),
    path ('blog' , views.blog , name = 'blog'),
    path ('candidate' , views.candidate , name = 'candidate'),
    path ('jobs' , views.jobs , name = 'jobs'),
    path ('contact' , views.contact , name = 'contact'),
    path ('single-blog' , views.single_blog , name = 'single-blog'),
    path ('elements' , views.elements , name = 'elements'),
    path ('post_jop' , views.post_jop , name = 'post_jop'),
    path ('login' , views.login , name = 'login'),
    path ('<slug:slug>' , views.job_details , name = 'job_details'),


   
]