from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError



# ValidationError
# def code_validation(value):
#     if value != StudentDetails.Student_Code:
#         raise ValidationError("Mismatched Student Code.. please check")
#


# Create your models here.
class StudentDetails(models.Model):

    sections = [('A', 'A'),('B', 'B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G')]
    class_list = [('PP','PP'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')]
    blood_group_list = [('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-')]
    gender_list =[('Male','Male'),('Female','Female')]

    Student_Code = models.CharField(max_length=17, unique=True)

    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100, blank=True)
    Surname = models.CharField(max_length=100)
    Date_of_Birth = models.DateField()

    Blood_Group =models.CharField(max_length=4, null=True, choices=blood_group_list)
    Gender = models.CharField(max_length=20, null=True, choices=gender_list)


    Class = models.CharField(max_length=2, choices=class_list)
    Section = models.CharField(max_length=2, choices=sections)

    Village = models.CharField(max_length=100)
    Geog = models.CharField(max_length=100)
    Dzongkhag = models.CharField(max_length=100)

    Present_Adress = models.CharField(max_length=200)

    Name_of_Father = models.CharField(max_length=100)
    Contact_No1 = models.IntegerField()
    Name_of_Mother = models.CharField(max_length=100)
    Contact_No2 = models.IntegerField()

    Profile_photo = models.ImageField(max_length=264, null=True, blank=True)

    Infomation_Entered_on = models.DateTimeField(default=timezone.now)

    # def clean(self):
    #     all_clean_data = super().clean()
    #     Student_Code = all_clean_data['Student_Code']
    #     Confirm_Student_Code = all_clean_data['Confirm_Student_Code']
    #
    #     if Student_Code!= Confirm_Student_Code:
    #         raise ValidationError ("Mismatched Student Code")

    def clean(self):
        self.First_Name = self.First_Name.capitalize()
        self.Middle_Name= self.Middle_Name.capitalize()
        self.Surname = self.Surname.capitalize()
        self.Village =self.Village.capitalize()
        self.Geog = self.Geog.capitalize()
        self.Dzongkhag = self.Dzongkhag.capitalize()
        self.Name_of_Father =self.Name_of_Father.capitalize()
        self.Name_of_Mother =self.Name_of_Mother.capitalize()

    # def clean(self):
    #     cleaned_data = super().clean()
    #     Student_Code = cleaned_data.GET['Student_Code']
    #     Confirm_Student_Code = cleaned_data.GET['Confirm_Student_Code']
    #     if Std_Code != V_code:
    #         raise forms.ValidationError('Student Code is not matching, please check')




    def __str__(self):
        return  str(self.Student_Code)+ self.First_Name

    def get_absolute_url(self):
        return reverse("studentinfo:detail",kwargs={'pk':self.pk})
