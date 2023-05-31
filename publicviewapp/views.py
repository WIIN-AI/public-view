from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'home.html', {'name': 'Wiinai kkumar'})


def dashboard(request):
    return HttpResponse("This is dashboard screen")


def add(request):
    # val1 = int(request.GET['num1'])
    # val2 = int(request.GET['num2'])

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    results = val1 + val2
    return render(request, "result.html", {"results": results})
