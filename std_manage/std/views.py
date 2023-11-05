from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def home(request):
    std = Student.objects.all()
    return render(request,"std/home.html", {'std':std})

def std_add(request):
    if request.method == 'POST':
        print("ADDED")
        stds_roll = request.POST.get("std_roll")
        stds_name = request.POST.get("std_name")
        stds_email = request.POST.get("std_email")
        stds_phone = request.POST.get("std_phone")
        stds_address = request.POST.get("std_address")
        stds_division = request.POST.get("std_division")

        s = Student()
        s.roll = stds_roll
        s.name = stds_name
        s.email = stds_email
        s.phone = stds_phone
        s.address = stds_address
        s.division = stds_division 

        s.save()
        return redirect('/std/home')

    return render(request,"std/add_std.html", {})

def std_delete(request,roll):
    s = Student.objects.get(pk=roll)
    s.delete()
    return redirect("/std/home")

def std_update(request,roll):
    std = Student.objects.get(pk=roll)
    return render(request,"std/update_std.html",{'std':std})

def do_std_update(request,roll):
    std_roll = request.POST.get("std_roll")
    std_name = request.POST.get("std_name")
    std_email = request.POST.get("std_email")
    std_phone = request.POST.get("std_phone")
    std_address = request.POST.get("std_address")  
    std_division = request.POST.get("std_division") 

    std = Student.objects.get(pk=roll)
    std.roll = std_roll
    std.name = std_name
    std.email = std_email
    std.phone = std_phone
    std.address = std_address
    std.division = std_division

    std.save()
    return redirect("/std/home")