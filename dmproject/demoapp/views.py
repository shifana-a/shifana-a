from django.shortcuts import render
from . models import service
from . models import team
# Create your views here.
def demo(request):
    obj=service.objects.all()
    ob=team.objects.all()
    return render(request,"index.html",{'result':obj,'res':ob})
