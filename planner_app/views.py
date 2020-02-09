from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import TaskForm
from .models import Task_Model
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')

        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,
                                                password=password1,
                                                email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                print('user created')

        else:
            messages.info(request, "password not matching...")
            return redirect('register')
        return redirect('login')

    else:
        return render(request, 'register.html')

def home(request):

    context = {
        'forms' : TaskForm(),
    }
    pagination = Paginator(Task_Model.objects.all().filter(user_id=request.user).order_by('end_date'), 4)

    context["tasks"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range


    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = request.user
            task.save()
        else:
            context['form'] = form


    return render(request, 'home.html', context)

def task_edit(request,id):
    task_data = Task_Model.objects.filter(id=id).first()
    context = {
        'edit_tasks': task_data,
        'form': TaskForm(instance=task_data)
    }
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task_data)
        if form.is_valid():
            task = form.save()
            # task.user_id = request.user
            return redirect('home')
    return render(request, 'includes/edit_form.html', context)


def task_delete(request,id):
    task_data = Task_Model.objects.filter(id=id).first()
    context = {
        'task_data' : task_data
    }

    if request.method == "DELETE":
        task_data.delete()
        return redirect('home')

    return render(request, 'includes/delete.html',context)


def filter_period_view(request, slug):
    context = {
        'forms': TaskForm(),
    }
    pagination = Paginator(Task_Model.objects.filter(user_id=request.user,task_periods=slug).order_by('end_date'), 4)

    context["tasks"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = request.user
            task.save()
        else:
            context['form'] = form
    return render(request, 'home.html',context)
