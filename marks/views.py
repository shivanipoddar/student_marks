from django.shortcuts import render
from django.contrib import messages
from .models import Marks


# Create your views here.
def home(request):
    return render(request, 'home.html')


def marks(request):
    if request.POST:
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        chemistry = request.POST.get('chemistry')
        math = request.POST.get('math')
        physics = request.POST.get('physics')
        total = request.POST.get('total')
        per = request.POST.get('per')
        m = Marks(name=name,roll_no=rollno,math=math,physics=physics,chemistry=chemistry,total=total,per=per)
        m.save()
        messages.success(request, 'successfuly added.')
        return render(request, 'marks.html')
    else:
        return render(request, 'marks.html')


def leaderboard(request):
    info = Marks.objects.order_by('-per')
    data = info.values('name', 'roll_no','total','per')
    return render(request, 'leaderboard.html', {'data':data})