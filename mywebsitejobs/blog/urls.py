from django.urls import path
from  . import views

app_name = "blog"

urlpatterns = [
    path ('', views.blog , name='blog'),
    path ('/single-blog', views.single_blog , name='single-blog'),
    
]