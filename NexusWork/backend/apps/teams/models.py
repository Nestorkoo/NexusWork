from django.db import models

class Team(models.Model):
    RANKS = [
        ('junior_team', 'Junior Team'),
        ('pro_team', 'Pro Team'),
        ('expert_team', 'Expert Team'),
    ]
    achievements = [ 
        ('team_of_the_month', 'Team of the Month'),
        ('team_of_the_year', 'Team of the Year'),
        ('team_of_the_decade', 'Team of the Decade'),
        ('speedster', 'Speedster'),
        ('team_with_the_highest_rating', 'Team with the Highest Rating'),
        ('the_team_that_completed_the_most_tasks', 'The Team That Completed the Most Tasks'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField('customuser.CustomUser', related_name='teams', blank=True)
    rank = models.CharField(max_length=20, choices=RANKS, default='junior_team')
    owner_id = models.ForeignKey('customuser.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    tasks = models.ManyToManyField('tasks.Task', related_name='teams', blank=True)
    achievement = models.CharField(max_length=150, choices=achievements, default='No achievements')
    tasks_completed = models. IntegerField(default=0)
    comment = models.ManyToManyField('comments.Comment', related_name='teams', blank=True)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ['-created_at']

    def set_new_rank(self):
        if self.score > 250:
            self.rank = 'pro_team'
        elif self.score > 600:
            self.rank = 'expert_team'
        else:
            self.rank = 'junior_team'
        self.save()
        
