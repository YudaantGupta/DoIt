from django.urls import path
from . import views
from django.shortcuts import redirect

def landing(request):
    return redirect("/dash")

urlpatterns = [
    path("dash/" , views.dash),
    path("",landing),
    path("grouping/new/" , views.new_grouping),
    path("entry/new/" , views.new_entry),
    path("grouping/<int:id>/" , views.grouping),
    path("grouping/delete" , views.delete),
    path("entry/<int:id>/" , views.entry ),
    path("entry/edit/<int:id>/" , views.entryedit ),
    path("search/" , views.search )
]
