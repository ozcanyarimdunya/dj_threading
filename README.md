# Django with multithreading 

Django background tasks with `threading` module. 

**NOTE:** No need celery anymore for single-time-run background tasks

Documentation: [https://ozcanyarimdunya.github.io/dj_threading/](https://ozcanyarimdunya.github.io/dj_threading/)

## How it works

1. User send a request to start a long running task
2. Django receives the thread and spawns a thread to do something else.
3. Thread starts working at background
4. Django finish his actions and send response to user
5. (Later) Thread finished

We created a django model when user starts a task and this model's id
sent to long running task as argument. 

We can get/change/save model in this task. During this time we can
access this model on any django view. 

So with this we can set custom status on model in task and access them
in anywhere at anytime.

## Usage and Installation on local

Install the requirements

```
make install 
``` 

Make database migrations

```
make migrations
```

Run the server and open a browser then navigate to *http://localhost:8000*

```
make start
```

## Usage and installation on Docker

Run below command and open a browser then navigate to
*http://localhost:8000*

```
make docker
```
