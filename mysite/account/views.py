# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate,login
# from .forms import LoginForm
#
# def user_login(request):
#     if request.method == "POST":
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             cd = login_form.cleaned_data
#             user = authenticate(username=cd['username'], password = cd["password"])
#
#             if user:
#                 login(reques,user)
#                 return HttpResponse("Welcome You! You have been aythenticated successfully")
#             else:
#                 return HttpResponse("Sorry. Your username or password is incorrect.")
#         else:
#             return HttpResponse("Invalid login")
#     if request.method == "GET":
#         login_form = LoginForm()
#         return render(request, 'account/login.html', {"form": login_form})

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd =login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request,user)
                return HttpResponse("Welcome You! You have been aythenticated successfully")
            else:
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})

from .forms import LoginForm, RegistrationForm

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, you can not register.")
    else:
        user_form = RegistrationForm()
        return render(request, "account/register.html",{"form": user_form})