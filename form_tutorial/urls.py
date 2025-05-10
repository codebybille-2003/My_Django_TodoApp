from django.urls import path
from . import views

urlpatterns=[
    path('info/',views.stu_info,name='info'),
]