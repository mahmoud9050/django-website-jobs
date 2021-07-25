from django import forms
from .models import Jobs

class JobsFormes(forms.ModelForm):
    class Meta:
        model = Jobs 
        fields = ['title','location','company','photo','description','Vacancy','price',
        'job_type','experience','responsibility','qualifications','category'] 