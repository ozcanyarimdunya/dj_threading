---
id: usage
title: Usage
sidebar_label: How to use ?
---

This document intend to explain **usage of threads in django** .

## Creating a model

Create a `Task` model. We will save thread status in this model

```python
class Task(models.Model):
    status = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    def set_status(self, status=None):
        print(status)  # or use logger
        self.status = status
        self.save()

    def get_status(self):
        return self.status

```


## Defining task starting view

```python
# url /start/

def start(request):
    """Start long running task"""

    task = Task.objects.create()
    t = threading.Thread(target=lambda: long_running_task(task.id))
    t.setDaemon(True)
    t.start()
    return JsonResponse({'message': 'Task started', 'taskId': task.id})
```

## Defining long running task

```python
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

```

## Defining task status view

```python
# url /status/<int:task-id>/

def status(request, task_id):
    """Check long running task status"""

    task = Task.objects.get(pk=task_id)
    message = task.get_status()
    return JsonResponse({'message': message, 'taskId': task_id})
```

## Invoking the api from ui

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Django with Threading</title>
</head>
<body>
<div class="main">
  <button class="start" onclick="onStart()">Start</button>
  <button class="status" onclick="onStatus()">Status</button>
  <p class="result" id="result"></p>
</div>
<script>
  let taskId;

  function onStart() {
    const url = "/start/";
    fetch(url)
      .then(resp => resp.json())
      .then(data => {
        taskId = data.taskId;
      })
  }

  function onStatus() {
    const url = "/status/" + taskId;
    fetch(url)
      .then(resp => resp.json())
      .then(data => {
        let result = document.getElementById('result');
        result.innerHTML = result.innerHTML + '<br>' + data.message;
      })
  }
</script>
</body>
</html>
```
