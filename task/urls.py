from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('task/<int:id>',views.task_details,name='task'),
     path('edit/<int:id>',views.edit_task,name='edit'),
      path('delete/<int:id>',views.delete_task,name='delete'),
]