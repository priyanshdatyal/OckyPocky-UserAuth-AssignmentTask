from django.core.checks import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def authenticatePage(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def signupuser(request):
    if request.method == 'POST':
        
        email=request.POST['email']
        username=request.POST['name']
        password1=request.POST['crpassword']
        password2=request.POST['cnpassword']
        contact=request.POST['contact']

        try:
            fisrt_name = username.split('_')[0]
            last_name = username.split('_')[1]
        except:
            messages.error(request,"Invalid Username- Correct Format : FirstName_LastName")
            return redirect('')

        if len(username)>30:
            messages.error(request,"Your username is too long")
            return redirect('')
        if password1!=password2:
            messages.error(request,"Passwords do not match")
            return redirect('')
        if len(contact)!=10 :
            messages.error(request,"Invalid Contact")
            return redirect('')

        username = username
        newUser = User.objects.create_user(username,email,password1)
        newUser.contact=contact
        newUser.first_name=fisrt_name
        newUser.last_name=last_name
        newUser.save()

        messages.success(request,"Hoorrayyyy! Your account has been created successfully")
        return redirect('home')

    else:
        return HttpResponse("Login Required")
    
def loginuser(request):   
    if request.method == 'POST':
        loginmail=request.POST['loginmail']
        loginpassword = request.POST['l_password']

        user = authenticate(username=loginmail,password=loginpassword)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/')

    else:
        return HttpResponse("NOT FOUND")

def logoutuser(request):   
    logout(request)
    messages.success(request,"Logged Out SuccessFully")
    return redirect('')