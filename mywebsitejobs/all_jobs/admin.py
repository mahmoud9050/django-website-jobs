from django.contrib import admin
from . models import Jobs , Category ,Apply

# Register your models here.

admin.site.register (Jobs) 
admin.site.register (Category) 
admin.site.register (Apply)