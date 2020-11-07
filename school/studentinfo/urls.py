"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from studentinfo import views



app_name = 'studentinfo'

urlpatterns =[
    # path('', views.StudentListView.as_view(), name='list'),
    path('',views.student_list, name='list'),
    path('<int:pk>', views.StudentDetailView.as_view(), name='detail'),
    path('create/', views.StudentCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.StudentDeleteView.as_view(), name='delete'),

]
