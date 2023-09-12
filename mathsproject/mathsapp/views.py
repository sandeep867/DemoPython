from django.shortcuts import render

from mathsapp.models import MyTable, NewTable


# Create your views here.
def fun(request):
    obj = MyTable.objects.all()
    obj1=NewTable.objects.all()

    return render(request, "index.html", {'result': obj,'result1':obj1})
# def add(request):
#     x=int(request.GET['num_1'])
#     y=int(request.GET['num_2'])
#     res=x+y
#     sub = x-y
#     mul = x*y
#     return render(request,"Result.html", {'Addition': res, 'Sub': sub, 'Mul': mul})
