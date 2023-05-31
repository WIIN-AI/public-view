from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == "POST":
        print(request.POST['user_name'])
        messages.info(request, "Checking the message/alert option with in ui")
        # return HttpResponse("Successfully Submitted Request")
        return redirect('signup')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        print(request.POST['user_name'])
        print(request.POST['pwd'])
        messages.info(request, "Checking the message/alert option with in ui")
        # return HttpResponse("Successfully Submitted Request")
        return redirect('/')
    else:
        return render(request, 'signup.html')


def logout(request):
    return redirect('/')
