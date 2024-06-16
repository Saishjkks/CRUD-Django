from django.shortcuts import render, HttpResponse, redirect
from home.models import Task


def home(request):
    context = {'success': False}
    
    if request.method == "POST":
        # Handle the form submission
        title = request.POST['title']
        desc = request.POST['desc']
        
        # Create a new Task object and save it to the database
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        
        # Update context to reflect success
        context = {'success': True}
    
    return render(request, 'index.html', context)

# Tasks view to display all tasks
def tasks(request):
    # Retrieve all tasks from the database
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    
    return render(request, 'tasks.html', context)

# Delete task view
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks')

# Update task view
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.taskTitle = request.POST['title']
        task.taskDesc = request.POST['desc']
        task.save()
        return redirect('/tasks')
    context = {'task': task}
    return render(request, 'update_task.html', context)
