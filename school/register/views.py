from django.shortcuts import render, redirect
from register.forms import RegisterForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# ?password change done

def password_change_done(request):
    return render(request, 'registration/password_change_done.html')

# registration
@login_required
def register(request):
     if request.method=="POST":
         form = RegisterForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/')
     else:
         form = RegisterForm()

     return render(request, 'register/register.html', {"form":form})


# LOGOUT
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# LOGIN
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')

        else:
            print("someone tried to login and failed")
            print("Username: {} and password: {}". format(username,password))
            return HttpResponse("login_error: Invalid User Details")

    else:
        return render(request, 'registration/login.html', {})
