from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import auth
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from main.models import Entry , Grouping

def signup(request):
    err = ""
    form = UserCreationForm()

    if request.method == "POST":
        submitted_form = UserCreationForm(request.POST)
        if submitted_form.is_valid():
            user = submitted_form.save()
            profile = Profile(user = user)
            profile.save()

            return redirect ("/accounts/login")
        else:
            err = "Username/password is incorrect"

    data = {
        "form":form,
        "err":err
        
    }
    return render(request, "accounts/signup.html",data)

def login(request):
    err = ""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username= username , password = password)

        if user:
            auth.login(request , user)
            return redirect("/dash")
        else:
            err = "Username/password is incorrect"
        
    data = {
        "err":err
    }

    return render(request, "accounts/login.html",data)

def profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(instance = profile)
        print(profile)

        if request.method == "POST":
            profile_form = ProfileForm(request.POST , instance = profile)
            request.user.first_name = request.POST["first"]
            request.user.last_name = request.POST["last"]
            request.user.save()


            if profile_form.is_valid():
                profile_form.save()
        
        data = {
            "profile_form":profile_form,
            "profile":profile
        }

        return render(request, "accounts/profile.html",data)
    
    else:
        return redirect("/accounts/login")

def logout(request):
    auth.logout(request)
    return render(request, "accounts/login.html")

def public(request, username):
    data = {}
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)



        public_entries = []
        for i in user.groupings.all():
            x = i.entries.filter(public = True)
            public_entries.append(x)
            print(x)


        data["public"] = public_entries
        data["u"] = user
        data["profile"] = profile

        print(public)



    except:
        pass

    return render(request, "accounts/public.html" , data)
