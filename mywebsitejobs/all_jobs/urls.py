from django.urls import path
from  . import views

app_name = "jobs"

urlpatterns = [
    path ('', views.jobs , name = 'jobs'),
    path ('post_job/', views.post_jop , name = 'post_job'),
    path ('<str:slug>/' , views.job_details , name = 'job_details'),


   
]