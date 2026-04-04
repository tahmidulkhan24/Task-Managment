from django.urls import path
from tasks.views import *

urlpatterns = [
    path('manager_dashboard/', manager_dashboard),
    path('user_dashboard/',user_dashboard),
    path('test/',test),
    path('task_form/',task_form,name="task_form"),
    path('view_task/',view_task)
]