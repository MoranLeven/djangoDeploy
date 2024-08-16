from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
from django.urls import path
from django.http import HttpResponse    
from django.db import models
from .models import User
import json


def crudOpsHome(request):
    return render(request,"home.html")

def createUser(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user_form = form.save(commit=False)
            # user_form.profilePicture = request.FILES['profilePicture'].read()
            user_form.save()
            return HttpResponse(f"User Created {request.POST['username']}")
    else:
        form = UserForm()
    return render(request,"createdata.html",{'form':form})

def getChangedData(keys,form):
    data = {changed_value:form.data[changed_value] for changed_value in keys}
    return json.dumps(data)

def updateUser(request):
    if request.method == "GET":
        uid = request.GET.get('userId')
        if uid:
            userData = User.objects.get(userId=uid)
            form = UserForm(instance=userData)
            return render(request, 'updatedata.html', {'form': form})
        else:
            return redirect("read")
    #when user wants to update the stuff haha
    elif request.method == "POST":
        uid = request.GET['userId']
        x = User.objects.get(userId=uid)
        userData = get_object_or_404(User, userId=uid)
        # Pass both POST data and the instance to be updated
        form = UserForm(request.POST, instance=userData)
        if form.is_valid():
            form.save()
        # else:
        return HttpResponse(getChangedData(form.changed_data,form))

class readUser(ListView):
    model = User
    template_name = 'readdata.html'  # Specify your template name/location
    context_object_name = 'userData'  # Specify the context object name


def deleteUser(request):
    return render(request,"deletedata.html")

def getDataById(request,id):
    user = User.objects.get(id=id)
    return render(request,"getById.html",{"data":user})



