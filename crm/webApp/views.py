from django.shortcuts import render, redirect
from .forms import CreateUserForm, LogınForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


from django.contrib.auth.decorators import login_required
from .models import Kayit

from django.contrib import messages
def home(request):
    return render(request, "webapp/index.html")


#! Register a user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User registration successful!')
            return redirect("my-login")
    context = {
        "form": form,
    }

    return render(request, "webapp/register.html", context=context)


#! Login a user
def my_login(request):
    form = LogınForm()

    if request.method == "POST":
        form = LogınForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request,'User has Logged successfully!')
                return redirect("dashboard")

    context = {"form": form}
    return render(request, "webapp/my-login.html", context=context)


# TODO Dashboard


@login_required(login_url="my-login")
def dashboard(request):
    my_records = Kayit.objects.all()

    context = {"records": my_records}
    return render(request, "webapp/dashboard.html", context=context)


#!create a record


@login_required(login_url="my-login")
def create_record(request):
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Your Record was created!')
            return redirect("dashboard")

    context = {"form": form}

    return render(request, "webapp/create-record.html", context=context)


#! Update a record
@login_required(login_url="my-login")
def update_record(request, pk):
    record = Kayit.objects.get(id=pk) #primary key = id yapıldı
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST,instance=record)

        if form.is_valid():
            form.save()
            messages.success(request,'Your record w as updated!')
            return redirect("dashboard")
        
    context = {"form": form}

    return render(request,'webapp/update-record.html',context=context)

# Read /View a singular record

@login_required(login_url="my-login")
def singular_record(request, pk):
    all_records = Kayit.objects.get(id=pk)

    context = {'record':all_records}
    return render(request,'webapp/view-record.html',context=context)
    

#!Delete Singular Record
@login_required(login_url="my-login")
def delete_record(request, pk):

        record = Kayit.objects.get(id=pk)
        record.delete()

        messages.success(request,'Your record has been deleted')
        return redirect("dashboard")

# ? User Log Out
def user_logout(request):
    auth.logout(request)
    messages.success(request,'Log Out Success!')
    return redirect("my-login")
