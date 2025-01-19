from django.db import models

class Task(models.Model):
    statuses = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled'),
        ('datermined', 'Determined'),
        ('on_hold', 'On Hold'),
        ('defferred', 'Deferred'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey('teams.Team', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=statuses, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('customuser.CustomUser', on_delete=models.CASCADE, related_name='created_tasks')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if self.status == 'completed':
            self.completed_at = models.DateTimeField(auto_now_add=True)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.assigned_to.tasks.remove(self)
    def delete_daterimined(self, *args, **kwargs):

        if self.status == 'datermined':
            super().delete(*args, **kwargs)
            self.assigned_to.tasks.remove(self)
