from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        #form is submitted
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user= authenticate(request, password='password', username='username')

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('User Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
        
    else:
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})

@login_required
def dashboard(request):
    return render(request,'accounts/dashboard.html',{'section':'dashboard'})

def user_registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid:
            new_user = user_form.save(commit=False)
            #set the chosen password
            new_user.set_password(new_user.cleaned_data['password'])
            new_user.save()

            return render(request,'accounts/register_done.html',{'new_user':new_user})

        else:
            user_form = UserRegistrationForm()
        return render(request,'accounts/register.html',{'user_form':user_form})







