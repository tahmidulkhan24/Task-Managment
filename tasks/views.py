from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def manager_dashboard(request):
    return render(request, "manager_dashboard.html")

def user_dashboard(request):
    return render(request,"user_dashboard.html")
def test(request):
    context={
        "name":['labib','khan','tk'],
        "age":23
    }
    return render(request,"test.html",context)
def task_form(request):
    if request.method == "POST":
        form = TaskModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Task Added Successfully!")
            return redirect('task_form')
    else:
        form = TaskModelForm()

    return render(request, "task_form.html", {"form": form})