from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register (request):
    if request.method=='POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
               user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)

            user.save();
            print("user created")
            return redirect('login')
        else:
            messages.info(request,"messages not matching")
            return redirect('register')
        # return  redirect('/')
    return render(request,"register.html")

# login
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is  not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login.html')

    return render(request,'login.html')

# logout
def logout (request):
    auth.logout(request)
    return redirect('/')
