from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #to pop flash messages

# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home') #akan tunjuk homepage
        else:
            messages.success(request, 'There was an error, please try again!')
            return redirect('home') #akan tunjuk login
    
    else:
        return render(request, 'website/home.html')

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out...')
    return redirect('home')

def register_user(request):
    return render(request, 'website/register.html',{
        
    })
