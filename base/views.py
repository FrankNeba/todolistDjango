from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import Todo
from .form import todocreates, Loginform

# Create your views here.
def todo_list(request):
    query = request.GET.get('q', '')
    todos = Todo.objects.filter(
        Q(title__contains = query) |
        Q(description__contains = query)
    )
    context = {'todos':todos}
    return render(request, 'base/todo_list.html', context)

def todocreate(request):
    # if request.method == 'POST':
    #     title = request.POST['title']
    #     description = request.POST['description']
    #     image = request.FILES['image']
    #     todo = Todo(title = title, description = description, image = image)
    #     todo.save()
    #     return redirect('addtodo')
    # return render(request, 'base/createtodo.html')
    form = todocreates()
    if request.method == 'POST':
        form = todocreates(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todolist')

    context = {'form': form}
    return render(request, 'base/todo_form.html', context)


def tododetails(request, id):
    todo = Todo.objects.get(pk=id)
    context = {'todo': todo}
    return render(request, 'base/todo_details.html', context)



def delete(request, pk):
    todo = Todo.objects.get(id=pk) 
    if request.method == 'POST':
        todo.delete()
        return redirect('todolist')
    return render(request, 'base/delete.html', {'todo': todo})

def todoupdate(request, pk):
    todo = Todo.objects.get(id=pk)
    form = todocreates(instance = todo)
    if request.method == 'POST':
        form = todocreates(request.POST, instance = todo)
        form.save()
        return redirect('todolist')
    return render(request, 'base/todo_form.html', { 'form':form})

def signup_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'base/signup.html', {'form':form})


def Loginuser(request):
    form = Loginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('todolist')
            return HttpResponse("user not found")
    context = {'form': form}
    return render(request, 'base/login.html' ,context)

def Logoutuser(request):
    logout(request)
    return redirect('todolist')
    








# def tododetails(request):
#     const = 1