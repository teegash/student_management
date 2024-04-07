from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_management_app.EmailBackEnd import EmailBackEnd


# Create your views here.
def showDescPage(request):
    return render(request, "demo.html")


# Function for showing login page
def ShowLoginPage(request):
    return render(request, "login_page.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")


# Creating get_user_details function
def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : " + request.user.email + " usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")


# Creating a function for logout
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
