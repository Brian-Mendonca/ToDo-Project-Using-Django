from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from .models import ToDo


def todo_list(request):
    ToDos = ToDo.objects.order_by('-id')
    in_progress_tasks = ToDo.objects.filter(completed = False).order_by('-id')
    completed_tasks = ToDo.objects.filter(completed = True).order_by('-id')
    return render(request, 'index.html',{'in_progress_tasks':in_progress_tasks,
            'completed_tasks':completed_tasks
            })

# Code to create a ToDo and send it to database
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ToDo.objects.create(title=title, description=description)
    return redirect('todo_list')    

# Code to mark a ToDo is  completed
def complete_todo(request,todo_id):   
    todo = get_object_or_404(ToDo, id = todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

# Code  for Undo of a Completed ToDo
def toggle_todo(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)
    todo.completed = not todo.completed  
    todo.save()
    return redirect('todo_list')

#  Code to Delete the ToDo
def delete_todo(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)
    todo.delete()
    return redirect('todo_list')

# Code to edit the ToDo
def edit_todo(request, todo_id):
    todo = get_object_or_404(ToDo, id = todo_id)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        todo.title = title
        todo.description = description
        todo.save()
        return  redirect('todo_list')
    return render(request,'edit_todo.html',{'task':todo})
