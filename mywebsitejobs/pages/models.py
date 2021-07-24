from django.db import models


# Create your models here.


from django.db import models
from django.db.models.fields.files import ImageField
from django.utils.text import slugify



# Create your models here.
class Category(models.Model):
    name =models.CharField(max_length=20)
    def __str__(self) :
        return self.name

def img_uplode(instance,filename):
    imgname , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class Jobs(models.Model):
    lest =[
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
               
    ]
    title = models.CharField(max_length=100,verbose_name='titel')
    location = models.CharField(max_length=200,null=True,blank=True)
    company = models.CharField(max_length=200,null=True,blank=True)
    photo =ImageField(upload_to='photos', null=True, blank=True )
    description = models.TextField(null=True,verbose_name='description') 
    published_at = models.DateField(auto_now=True ) 
    Vacancy = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='price')  
    job_type = models.CharField(max_length=50,null=True,blank=True,choices=lest)
    experience = models.CharField(max_length=200,null=True,blank=True)
    responsibility = models.CharField(max_length=200,null=True,blank=True)
    qualifications = models.CharField(max_length=200,null=True,blank=True)
    category =models.ForeignKey(Category,on_delete=models.PROTECT,null=True, blank=True)

    def __str__(self) :
        return self.title




