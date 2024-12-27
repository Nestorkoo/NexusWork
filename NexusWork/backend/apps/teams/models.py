from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField('customuser.CustomUser', related_name='teams', blank=True)
    space_id = models.ForeignKey('spaces.Space', on_delete=models.CASCADE)
    tasks = models.ManyToManyField('tasks.Task', related_name='teams', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

