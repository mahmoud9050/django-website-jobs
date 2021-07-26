from django.urls import path
from  . import views


urlpatterns = [
    path ('' , views.jobs , name = 'a'),
    path ('post_job', views.post_jop , name = 'post_job'),
    path ('<str:slug>' , views.job_details , name = 'job_details'),


   
]