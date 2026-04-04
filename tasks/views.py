from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q ,Count,Min,Max#q diye or bujhay

# Create your views here.

def manager_dashboard(request):
    task = Task.objects.select_related('details').prefetch_related('assigned_to')
    #total
    counts=Task.objects.aggregate(
        total=Count('id'),
        complate=Count('id',filter=Q(status="COMPLETED")),
        in_prog=Count('id',filter=Q(status="IN_PROGRESS")),
        pending=Count('id',filter=Q(status="PENDING"))
    )
    # total=task.count()
    # complate=task.filter(status="COMPLETED").count()
    # in_prog=task.filter(status="IN_PROGRESS").count()
    # pending=task.filter(status="PENDING").count()
    contex={
        "task":task,
        "counts":counts
    }

    return render(request, "manager_dashboard.html",contex)

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
def view_task(request):
    #retrieve all data
    task=Task.objects.all()
    #retrieve a specific data
    task3=Task.objects.get(id=3)
    #to filter data
    taskf=Task.objects.filter(status="PENDING")
    #show the task which priority is not low
    taskp=TaskDetail.objects.exclude(priority="L")
    task5=Task.objects.filter(id__in=[1,5,7])
    taskq=Task.objects.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))
    #join (select related work on only one to one)
    join=Task.objects.select_related("details").all()
    # prefetch_related work for many to many or fk
    #jodi related name set na thake tobe module_set aivabe likte hoy
    project =Project.objects.prefetch_related('task_set').all()
    #aggregation
    task_cnt=Task.objects.aggregate(num_of_task=Count('id'))
    return render(request,"view_task.html",{"task":task,"task3":task3,"taskf":taskf,"taskp":taskp,"task5":task5,"taskq":taskq,"join":join,"project":project,"task_cnt":task_cnt})