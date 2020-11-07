from django import forms
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import  User
from django.contrib.auth.forms import  UserCreationForm


class RegisterForm(UserCreationForm):
    email= models.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
