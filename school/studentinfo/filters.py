import django_filters
from .models import *

class StudentFilter(django_filters.FilterSet):

    class Meta:
        model= StudentDetails
        fields = ['Student_Code','First_Name','Class','Section']
