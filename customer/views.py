from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User
from django.contrib.auth.hashers import check_password

# Create your views here.
def index(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request,"about_Us.html")

def contactus(request):
    return render(request,"Contact Us.html")

def safety(request):
    return render(request,"safety.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request, "signup.html")

def success(request):
    return render(request, "success.html")

def addUser(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone_no = request.POST.get('phone_no')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check if passwords match
        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        # Create the user object
        user = User.objects.create(
            fullname=fullname,
            phone_no=phone_no,
            gender=gender,
            dob=dob,
            email=email,
            password=password
        )
        
        # Save the user object
        user.save()
        
        # Redirect to a success page or another URL
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'signup.html')
    

# def validateUser(request):
#     if request.method == 'post':
#         phone_no = request.POST.get('phone_no')
#         password = request.POST.get('password')
        
def validateUser(request):
    
    if request.method == 'POST':
        print("here dd")
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')
        print(password)
        print(phone_no)
        # Query the User model based on the provided phone number
        try:
            user = User.objects.get(phone_no=phone_no)
        except User.DoesNotExist:
            # Handle case where user with given phone number does not exist
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        print(user)
        print(user.password)
        # Check if the provided password matches the user's password in the database
        if password != user.password:
            # Handle case where passwords do not match
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        print("here also")
        # Redirect to a success page or another URL
        return HttpResponseRedirect(reverse('success_page'))
    else:
        print("here")
        # Handle case where method is not POST
        return render(request, 'login.html')