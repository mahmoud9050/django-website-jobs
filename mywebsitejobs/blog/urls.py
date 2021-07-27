from django.urls import path
from  . import views

app_name = "blog"

urlpatterns = [
    path ('', views.blog , name='blog'),
    path ('<str:slug>/', views.single_blog , name='single-blog'),
    
]