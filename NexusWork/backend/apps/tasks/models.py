from django.db import models

class Task(models.Model):
    statuses = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey('customuser.CustomUser', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('customuser.CustomUser', on_delete=models.CASCADE, related_name='created_tasks')