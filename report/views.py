from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required

def log_in(request):

    if request.method == "POST":
        form = dict(request.POST)
        user = authenticate(username = form["username"][0],password=form["password"][0])
        login(request,user,)
        return redirect("report")
    return render(request,"login.html")

def log_out(request):
    logout(request)
    return redirect("login")

@login_required (login_url='login')
def report(request):

    region = Region.objects.all()
    items = Data.objects.all()
    selected=None
    data = {}
    if request.method == "POST":
        form = dict(request.POST)
        if form["region"][0] != "0":
            items = Data.objects.filter (region_id=form["region"][0])
            selected = int(form["region"][0])
        else:
            items = Data.objects.all ( )
            selected = "0"
    for item in items:
        if item.date in data.keys():
            data[item.date][0] += item.loaded_boxes
            data[item.date][1] += item.returned_boxes
        else:
            data[item.date]=[]
            data[item.date].append(item.loaded_boxes)
            data[item.date].append(item.returned_boxes)
    lables = [item.strftime("%d-%m-%Y") for item in data.keys() ]
    loaded = [item[0] for item in data.values()]
    returned = [item[1] for item in data.values()]
    context = {
        "lables":lables,
        "loaded":loaded,
        "returned":returned,
        "region": region,
        "selected":selected
    }
    return render(request,"report.html",context)


