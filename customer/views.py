from genericpath import exists
from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User,ContactQuery

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

def adminlogin(request):
    return render(request, "adminlogin.html")

def driverLogin(request):
    return render(request, "driverLogin.html")

def validateDriver(request):
    pass

def sendOTP(request):
    pass

def validateOTP(request):
    pass

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
        # Handle password mismatch error
        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        
        if len(phone_no) < 10 or len(phone_no) > 10:
            return render(request, 'signup.html', {'error': f'Invalid Phone Number!'})
        
        if User.objects.filter(phone_no=phone_no).exists():
            return render(request, 'signup.html', {'error': f'The Phone Number {phone_no} has already been used '})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': f'The Email Address {email} has already been used.'})
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
    
from django.shortcuts import render, redirect
from .models import DriverDetails

def addDriver(request):
    if request.method == 'POST':
        # Retrieve data from the form
        fullname = request.POST.get('fullname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        license = request.POST.get('license')
        vehicle_reg = request.POST.get('vehicle_reg')
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        routing_number = request.POST.get('routing_number')
        vehicle_make = request.POST.get('vehicle_make')
        vehicle_model = request.POST.get('vehicle_model')
        vehicle_color = request.POST.get('vehicle_color')
        agreement = request.POST.get('agreement') == 'on'

        # Create a new DriverDetails object
        driver = DriverDetails.objects.create(
            fullname=fullname,
            dob=dob,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            license=license,
            vehicle_reg=vehicle_reg,
            bank_name=bank_name,
            account_number=account_number,
            routing_number=routing_number,
            vehicle_make=vehicle_make,
            vehicle_model=vehicle_model,
            vehicle_color=vehicle_color,
            agreement=agreement
        )

        # Save the object
        driver.save()

        # Redirect to a success page or another URL
        return redirect('adminlogin')
    else:
        return render(request, 'adminlogin.html')



def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        user_type = request.POST.get('user_type')
        query_type = request.POST.get('query_type')
        comment = request.POST.get('comment')

        # Create the ContactQuery object
        query = ContactQuery.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            user_type=user_type,
            query_type=query_type,
            comment=comment
        )
        # Save the query object
        query.save()
        
        # Redirect to a success page or another URL
        return redirect('contactus')  # Provide the URL name for the success page
    else:
        return render(request, 'Contact Us.html')

