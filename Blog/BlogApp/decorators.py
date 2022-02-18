from django.shortcuts import redirect
from django.urls import reverse

def autheticated_user(view_f):

    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("BlogApp:Home"))
        else:
            return view_f(request, *args, **kwargs)

    return wrapper_fun

