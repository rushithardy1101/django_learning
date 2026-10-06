from django.db import models
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    status = models.CharField(max_length=20)
    priority=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)