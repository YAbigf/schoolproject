from django.urls import path 
from . import views
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("accounts/signup", views.signup, name="signup"), 
    path("accounts/signin", views.signin, name="signin"), 

]
