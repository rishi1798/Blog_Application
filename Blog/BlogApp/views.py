from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import BlogForm, SIgnUpForm
from .models import Blog
from .decorators import autheticated_user

from datetime import datetime
# Create your views here.

def demo(request):
    return HttpResponse("Hello world!!!!!!!!!!!!!!!!!!!")

@autheticated_user
def SignUpView(request):
    fm = SIgnUpForm()

    if request.method=="POST":
        print("4")
        fm= SIgnUpForm(request.POST)
        print("1")
        print(fm.errors)
        if fm.is_valid():
            print("2")
            fm.save()

            print("3")
            return HttpResponseRedirect(reverse("BlogApp:Login"))

    ctx = {"form":fm}
    return render(request, 'BlogApp/signup.html', context=ctx)

@autheticated_user
def LoginView(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse("BlogApp:Home"))

    return render(request, 'BlogApp/login.html')

@login_required(login_url="BlogApp:Login")
def LogOutView(request):

    logout(request)

    return HttpResponseRedirect(reverse("BlogApp:Login"))


@login_required(login_url="BlogApp:Login")
def Home(request):
    if request.method=="POST":
        fm=BlogForm(request.POST, request.FILES)

        if fm.is_valid():
            data = fm.save(commit=False)
            data.publish_date = datetime.now()
            data.update_date = datetime.now()
            # pass
            fm.save()

            return HttpResponseRedirect(reverse("BlogApp:List"))
    
    
    fm = BlogForm()
    ctx = {"form":fm}
    return render(request, "BlogApp/Home.html", context=ctx)

@login_required(login_url="BlogApp:Login")
def ListBlog(request):

    all_blog = Blog.objects.all()

    ctx = {"Blogs":all_blog}

    return render(request, "BlogApp/ListBlog.html", context=ctx)

@login_required(login_url="BlogApp:Login")
def DetailBlog(request,id):

    blogDetail = Blog.objects.get(id=id)

    ctx = {"BlogDetail":blogDetail}

    return render(request, "BlogApp/Detail.html", context=ctx)


@login_required(login_url="BlogApp:Login")
def EditBlog(request,pk):

    EditBlog = Blog.objects.get(id=pk)

    fm= BlogForm(instance=EditBlog)

    if request.method=="POST":
        fm = BlogForm(request.POST,request.FILES, instance=EditBlog )

        if fm.is_valid():
            data = fm.save(commit=False)

            data.update_date = datetime.now()

            fm.save()
            return HttpResponseRedirect(reverse("BlogApp:List"))




    return render(request, "BlogApp/Home.html", context={"form":fm})

@login_required(login_url="BlogApp:Login")
def DeleteBlog(request,pk):

    DelBlog = Blog.objects.get(id=pk)

    DelBlog.delete()


    return HttpResponseRedirect(reverse("BlogApp:List"))




def checkUsername(request):
    username = request.GET.get("user")

    avail_user = User.objects.filter(username=username)

    resData ={'available':False} 
    status = 200
    if len(avail_user)>0:
        resData["available"]=False
        status=409
    else:
        resData["available"]=True

    return JsonResponse(resData, status=status)
    
