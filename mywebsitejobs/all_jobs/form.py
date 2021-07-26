from django import forms
from .models import Jobs , Apply

class JobsFormes(forms.ModelForm):
    class Meta:
        model = Jobs 
        fields = ['title','location','company','photo','description','Vacancy','price',
        'job_type','experience','responsibility','qualifications','category'] 


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','cv','cover_letter']