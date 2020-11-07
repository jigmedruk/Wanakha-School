from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.forms.widgets import SelectDateWidget
from studentinfo.filters import StudentFilter
from studentinfo.models import StudentDetails


# Create your views here.

class IndexView(TemplateView):
    template_name= 'index.html'

# class StudentListView(ListView):
#
#     context_object_name = 'student_list'
#     model = models.StudentDetails
#     template_name = 'studentinfo/student_list.html'

def student_list(request):
    std_details =  StudentDetails.objects.order_by('id')
    myFilter = StudentFilter(request.GET, queryset=std_details)
    std_details =myFilter.qs
    std_dicts = {"student_list":std_details, 'myFilter':myFilter}
    return render(request, 'studentinfo/student_list.html', context=std_dicts)



class StudentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = models.StudentDetails
    template_name = 'studentinfo/student_detail.html'


# 

class StudentCreateView(CreateView):
    fields= '__all__'
    model = models.StudentDetails

    def get_form(self):
        '''add date picker in forms'''
        form = super(StudentCreateView, self).get_form()
        form.fields['Date_of_Birth'].widget = SelectDateWidget()
        return form



class StudentUpdateView(UpdateView):
    fields = ('Gender','Class', 'Section','Present_Adress','Contact_No1','Contact_No2', 'Blood_Group','Profile_photo')
    model = models.StudentDetails

class StudentDeleteView(DeleteView):
    model = models.StudentDetails
    success_url = reverse_lazy("studentinfo:list")
