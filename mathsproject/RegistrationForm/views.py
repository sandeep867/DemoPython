from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid login or please complete your registration form")
            return redirect('game')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['Lastname']
        email = request.POST['E-Mail']
        password = request.POST['password']
        confirmpassword = request.POST['confirm Password']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,email=email, password=password)
                user.save()
                print("user registered")
                return redirect('login')

        else:
            messages.info(request,"Password is invalid")
            return redirect('register')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
