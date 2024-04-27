from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index",views.index, name="index"),
    path("aboutUs", views.aboutus, name="aboutus"),
    path("contactUs", views.contactus,name="contactus"),
    path("safety",views.safety,name="safety"),
    path("login",views.login,name="login"),
    path("signUp",views.signup,name="signup"),
    path("addUser", views.addUser, name="addUser"),
    path("afterLogin", views.validateUser, name="validate"),
    path("success", views.success, name="success_page"),
    path("admin", views.adminlogin, name="adminlogin"),
    path("addDriver", views.addDriver, name="addDriver"),
    path("addContact", views.contact_us, name="addcontact")
]
