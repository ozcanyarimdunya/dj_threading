from django.db import models


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
