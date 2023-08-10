from django.shortcuts import render,redirect
from .models import Grouping , Entry
from .forms import EntryForm
from django.contrib.auth.models import User

def dash(request):
    if request.user.is_authenticated:
        data = {}
    else:
        return redirect("/accounts/login")

    return render(request, "main/dash.html",data)

def new_grouping(request):

    if request.user.is_authenticated:
        data = {}
        if request.method == "POST":
            grouping = Grouping(title=request.POST["title"] , user = request.user)
            grouping.save()
            return redirect ("/dash")
    
    else:
        return redirect("/accounts/login")
    
    return render(request , "main/new_grouping.html",data)

def new_entry(request):

    if request.user.is_authenticated:
        data = {}

        entry_form = EntryForm()
        data["entry_form"] = entry_form
        entry_form.fields["grouping"].queryset = request.user.groupings

        if request.method == "POST":
            entry_form = EntryForm(request.POST , request.FILES)
            if entry_form.is_valid():
                entry = entry_form.save()
                g_id = entry.grouping.id

                return redirect(f"/grouping/{g_id}/")

    
    else:
        return redirect("/accounts/login")
    
    return render(request , "main/new_entry.html",data)

def grouping(request , id):

    if request.user.is_authenticated:
        data = {}
        grouping = Grouping.objects.get(id=id)
        if grouping.user == request.user:
            data["grouping"] = grouping
            return render(request, "main/grouping.html",data)
        else:
            return redirect("/")
    
    else:
        return redirect("/accounts/login")
    
    return render(request , "main/grouping.html",data)

def delete(request):
    
    if request.user.is_authenticated:
        grouping = Grouping.objects.get(id = request.GET["g_id"])
        if grouping.user == request.user:
            grouping.delete()
            return redirect("/")
        else:
            pass
    return redirect("/dash")

def entry(request,id):
    data = {}
    if request.user.is_authenticated:
        entry = Entry.objects.get(id = id)
        data["entry"] = entry
        return render(request , "main/entry.html" , data)
    else:
        return redirect("/")

def entryedit(request,id):
    data = {}

    if request.user.is_authenticated:
        entry = Entry.objects.get(id = id)

        if request.method == "POST":
            entry_form = EntryForm(request.POST, request.FILES, instance = entry)

            if entry_form.is_valid():
                entry = entry_form.save()
                return redirect(f"/entry/{id}")


        if request.user == entry.grouping.user:
            entry_form = EntryForm(instance = entry)
            data["editform"] = entry_form 

            
        

        else:
            return redirect("/")
    else:
        return redirect("/accounts/login")

    return render(request , "main/editentry.html" , data)

def search(request):
    data = {}
    if request.user.is_authenticated:
        query = request.GET.get("query")

        results = None
        print(query)

        if query:
            results = User.objects.filter(username__contains = query)
            

            data["results"] = results
            print(results)
        




    return render(request, "main/search.html" , data) 




