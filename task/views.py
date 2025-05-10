from django.shortcuts import render,redirect
from .models import MyTask
# Create your views here.
def home(request):
    task=MyTask.objects.all().order_by('id')
    if request.method=='POST':
       tname=request.POST['tname']
       tdesc=request.POST['tdesc']
       MyTask.objects.create(
          name=tname,
          desc=tdesc
       )
       return redirect('home')
    context={
        'task':task
    }
    return render(request,'home.html',context)

def task_details(request,id):
  data=MyTask.objects.get(id=id)
  context={
     'data':data
  }
  return render(request,'task.html',context)

def edit_task(request,id):
   task=MyTask.objects.get(id=id)
   if request.method=='POST':
      task.name=request.POST['tname']
      task.desc=request.POST['tdesc']
      task.save()
      return redirect('home')
   context={
      'task':task
   }
   return render(request,'form.html',context)

def delete_task(request,id):
   task=MyTask.objects.get(id=id)
   task.delete()
   return redirect('home')