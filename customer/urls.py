from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Index.html",views.index, name="index"),
    path("About_Us.html", views.aboutus, name="aboutus"),
    path("Contact Us.html", views.contactus,name="ContactUs"),
    path("Safety.html",views.safety,name="Safety"),
    path("login.html",views.login,name="login"),
    path("signup.html",views.signup,name="signup"),
    path("addUser", views.addUser, name="addUser"),
    path("afterlogin", views.validateUser, name="validate"),
    path("success", views.success, name="success_page")
]
