import datetime
from pydoc import describe
from urllib.request import Request
from todolist.models import Task
from todolist.forms import InputTask
from email import contentmanager
from multiprocessing import context
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# Method untuk resgister akun todolist
def register_todolist(request):
    form = UserCreationForm()
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# Method untuk login akun todolist
def login_user_todolist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # Melakukan login
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # Membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # Membuat dan menambahkan cookie last login ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Method untuk proses logout akun
def logout_user_todolist(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

# Method untuk membuat task baru
@login_required(login_url='/todolist/login')
def create_task(request):
    form = InputTask(request.POST)
    response = HttpResponseRedirect(reverse("todolist:show_todolist"))
    
    #Referensi : https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
    if form.is_valid() and request.method == 'POST':
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.date = datetime.datetime.now()
        new_task.save()
        form.save_m2m()
        return response
    
    context = {
        'form' : form
    }
    return render(request, 'create_task.html', context)

# Method untuk menambahkan task secara asinkronus pada template html
@login_required(login_url='/todolist/login')
def add_task_ajax(request):
     
    if request.method == "POST":        
        user_logged_in = request.user
        title = request.POST.get("title")
        date = datetime.datetime.now()
        description = request.POST.get("description")

        new_task = Task(user=user_logged_in,title=title, date=date, description=description)
        new_task.save()

        return HttpResponse(status=200)

    return redirect("todolist:show_todolist")

# Method untuk menampilkan task ke dalam todolist.html
@login_required(login_url='/todolist/login')
def show_todolist(request):
    user_logged_in = request.user
    data_todolist_user = Task.objects.filter(user=user_logged_in)
    context = {
        'nama' : 'Danendra Herdiansyah',
        'NPM' : '2106707012',
        'username'  : user_logged_in.username,
        'list_todolist_user' : data_todolist_user,
    }
    return render(request, "todolist.html", context)

# Method untuk menampilan task berbentuk json
@login_required(login_url='/todolist/login')
def show_todolist_json(request):
    data_todolist_user = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data_todolist_user), content_type="application/json")