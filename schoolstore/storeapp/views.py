from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from django.http import JsonResponse

from .form import MyForm



# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['psw']
        cnf = request.POST['cnf']

        if psw== cnf:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register.html')
            else:
               user=User.objects.create_user(username=username,password=psw)

            user.save();
            print("user created")
            return redirect('login.html')

    return render(request,"register.html")
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new.html')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login.html')

    return render(request,"login.html",)

def new(request):


    return render(request,"new.html")








def form(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            mail = form.cleaned_data['mail']
            address = form.cleaned_data['address']
            department = form.cleaned_data['department']
            courses = form.cleaned_data['courses']
            purpose = form.cleaned_data['purpose']
            materials = form.cleaned_data['materials']
            form.save()
        return redirect("sucess.html")



    return render(request, 'form.html', {'form': form})


def sucess(request):
    return render(request,"sucess.html")
def logout (request):
    auth.logout(request)
    return redirect('/')