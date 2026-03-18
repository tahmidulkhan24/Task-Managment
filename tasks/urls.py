
from django.urls import path
from tasks.views import contact

urlpatterns = [
   path('contact/',contact)
]
