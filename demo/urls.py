from django.urls import path

from .views import index, start, status

app_name = 'demo'
urlpatterns = [
    path('', index),
    path('start/', start),
    path('status/<int:task_id>/', status),
]
