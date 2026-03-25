from django.shortcuts import render
from django.http import HttpResponse

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