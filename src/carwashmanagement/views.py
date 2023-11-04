from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *

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

#logout users
def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect('login')

#register users
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_list(request):
    customers = Customer.objects.all().order_by('-timestamp')
    context = {'customers': customers}
    return render(request, 'CustomerRecord.html', context)

def customer_record(request, pk):
     if request.user.is_authenticated:
          #look up records
          customer_record = Customer.objects.get(id=pk)
          context = {'customer_record':customer_record}
          return  render(request, 'record.html', context)
     else:
          messages.warning(request, 'Must be logged in as Company employee to view record')
          return redirect('login')
#deletet record
def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Customer.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('customer-list')
	else:
		messages.success(request, "You Must Be Logged In To Delete records")
		return redirect('home')

def add_Customer(request):
	form = AddCustomerForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_customer = form.save()
				messages.success(request, "Customer Record Added Succesfull")
				return redirect('customer-list')
		return render(request, 'add_customer.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To Add Records")
		return redirect('home')
	
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Customer.objects.get(id=pk)
		form = AddCustomerForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')