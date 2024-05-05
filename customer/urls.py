from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index",views.index, name="index"),
    path("aboutUs", views.aboutus, name="aboutus"),
    path("contactUs", views.contactus,name="contactus"),
    path("safety",views.safety,name="safety"),
    path("login",views.loginu,name="login"),
    path("signUp",views.signup,name="signup"),
    path("addUser", views.addUser, name="addUser"),
    path("afterLogin", views.validateUser, name="validate"),
    path("success", views.success, name="success_page"),
    path("adminlogin", views.adminlogin, name="adminlogin"),
    path("addDriver", views.addDriver, name="addDriver"),
    path("addContact", views.contact_us, name="addcontact"),
    path("driverLogin", views.driverLogin, name="driverLogin"),
    path("validateDriver", views.validateDriver, name="validateDriver"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("submit-ride-request", views.submitRideRequest, name="submit-ride-request"),
    path("submit-ride-request", views.submitRideRequest, name="submit-ride-request"),
    path("availability", views.availability, name="availability"),
    path("rideaccept", views.rideaccept, name="rideaccept"),
    path("validateAdmin", views.validateAdmin, name="validateAdmin"),
    path("adminl", views.admin, name="adminl"),
    path("acceptRide", views.acceptRide, name="acceptRide")
]
