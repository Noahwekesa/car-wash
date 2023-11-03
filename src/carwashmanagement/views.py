from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#home page
def home(request):
    return render(request, 'index.html', {})

#login function
def login_user(request):
    #check to see if login in
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #if user is authenticated open dashboard
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Invalid email or password. Please try again.")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect('login')