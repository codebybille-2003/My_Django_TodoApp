from django.shortcuts import render

# Create your views here.
def stu_info(request):
    # print(request.__dict__)
    print(request.POST['name'])
    # print(request.GET['name'])
    # print(request.GET['email'])
    return render(request,'info.html')