from django.db import models

class Space(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey('customuser.CustomUser', on_delete=models.CASCADE)
    members = models.ManyToManyField('customuser.CustomUser', related_name='spaces', blank=True)
    teams = models.ManyToManyField('teams.Team', related_name='spaces', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name