from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=50)
    def __str__(self) :
        return self.name

def img_uplode(instance,filename):
    imgname , extension = filename.split(".")
    return "photos/%s.%s"%(instance.id,extension)

class Blog(models.Model):
    blog_name =models.CharField(max_length=200)
    description =models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True ) 

    photo = models.ImageField(upload_to=img_uplode)
    comments =models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category =models.ForeignKey(Category,on_delete=models.PROTECT,null=True, blank=True)
    slug =models.SlugField(max_length=400 , null=True, blank=True,unique=True)


    def save(self,*args,**kwargs):
      
        self.owner =(self.user )
        super(Blog,self).save(*args,**kwargs)


    def save(self,*args,**kwargs):
      
        self.slug = slugify(self.blog_name ,allow_unicode=True)
        super(Blog,self).save(*args,**kwargs)

      
    
    def __str__(self):
        return str (self.blog_name)
