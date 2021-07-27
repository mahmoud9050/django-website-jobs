import django_filters
from .models import Jobs

class JobsFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    experience = django_filters.CharFilter(lookup_expr='icontains')
    company = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Jobs
        fields =['title','location','experience','company','price','category','job_type']
 #
 # 
 # 
 # exclude = ['photo','published_at',,'Vacancy','price','description','category','qualifications','responsibility']