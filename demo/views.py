import threading

from django.http import JsonResponse
from django.shortcuts import render

from .models import Task


def index(request):
    """Index page"""

    return render(request, template_name='index.html')


def start(request):
    """Start long running task"""

    task = Task.objects.create()
    t = threading.Thread(target=lambda: long_running_task(task.id))
    t.setDaemon(True)
    t.start()
    return JsonResponse({'message': 'Task started', 'taskId': task.id})


def status(request, task_id):
    """Check long running task status"""

    task = Task.objects.get(pk=task_id)
    message = task.get_status()
    return JsonResponse({'message': message, 'taskId': task_id})


def long_running_task(task_id):
    """A long running task"""

    from time import sleep

    task = Task.objects.get(pk=task_id)
    task.set_status('1.STEP')
    sleep(1)
    task.set_status('2.STEP')
    sleep(2)
    task.set_status('3.STEP')
    sleep(3)
    task.set_status('4.STEP')
    sleep(4)
    task.set_status('5.STEP')
    sleep(5)
    task.set_status('FINISHED')
