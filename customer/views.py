from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User,ContactQuery
import random
from .models import DriverDetails,RideRequest
from datetime import datetime
from django.http import HttpResponse

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



def submitRideRequest(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        user_id = request.POST.get('user_id')
        pickup_location = request.POST.get('pickup_location')
        dropoff_location = request.POST.get('dropoff_location')
        
        # Get current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        try:
            # Convert current time string to datetime object
            pickup_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
        except ValueError:
            # Handle invalid time format
            return HttpResponse("Invalid time format")
        
        ride_type = request.POST.get('ride_type')
        
        # Get all available drivers
        available_drivers = DriverDetails.objects.filter(available=True)
        
        # Store ride request data in each available driver's ride_request_data field
        for driver in available_drivers:
            # Create a new instance of RideRequest
            ride_request = RideRequest.objects.create(
                user_id=user_id,
                pickup_location=pickup_location,
                dropoff_location=dropoff_location,
                pickup_time=pickup_time,
                ride_type=ride_type,
                driver=driver  # Assuming there's a ForeignKey field named 'driver' in RideRequest model
            )
            
        try:
            user = User.objects.get(fullname=user_id)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
        if not available_drivers:
            return render(request, 'success.html',{"user" : user,"warning":"Sorry Currently there is no available Rides"})
            # Save the ride request instance
        ride_request.save()
        # Redirect the user to a success page
        return render(request, 'success.html',{"user" : user,"success":"Your Request has been Sent."})
    else:
        # Handle case where method is not POST
        return render(request, 'ride_request_form.html')


def dashboard(request):
    return render(request, template_name="dashboard.html")

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
    


def validateUser(request):
    if request.method == 'POST':
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(phone_no=phone_no)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
        if password != user.password:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
        # Pass user data to the success.html template
        return render(request, 'success.html', {'user': user})
    else:
        return render(request, 'login.html')


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

