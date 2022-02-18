from django.urls import path
from . import views


app_name = "BlogApp"

urlpatterns = [
path("demo",views.demo,name="demo"),
path("home",views.Home,name="Home"),
path("",views.LoginView,name="Login"),
path("logout",views.LogOutView,name="Logout"),
path("register",views.SignUpView,name="Register"),
path("list",views.ListBlog,name="List"),
path("detail/<int:id>",views.DetailBlog,name="Detail"),
path("edit/<int:pk>",views.EditBlog,name="Edit"),
path("delete/<int:pk>",views.DeleteBlog,name="Delete"),
path("check-username",views.checkUsername,name="check")
]