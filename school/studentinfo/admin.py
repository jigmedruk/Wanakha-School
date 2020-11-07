from django.contrib import admin
from studentinfo.models import StudentDetails
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('Student_Code', 'First_Name', 'Middle_Name', 'Surname', 'Class', 'Section')
    search_fields = ('Student_Code', 'First_Name', 'Class', 'Section')

    filter_horizontal = ()
    list_filter =()
    fieldsets = ()

admin.site.register(StudentDetails, ItemAdmin)
