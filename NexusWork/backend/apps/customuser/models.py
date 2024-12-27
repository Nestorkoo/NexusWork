from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
from backend.apps.spaces.models import Space

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('junior', 'Junior Developer'),
        ('middle', 'Middle Developer'),
        ('senior', 'Senior Developer'),
        ('project_manager', 'Project Manager'),
        ('team_lead', 'Team-Lead'),
        ('backend', 'Backend Developer'),
        ('frontend', 'Frontend Developer'),
        ('devops', 'DevOps Engineer'),
        ('qa_engineer', 'QA Engineer'),
        ('automation_qa_engineer', 'Automation QA Engineer'),
        ('ui/ux_designer', 'UI/UX Designer'),
        ('graphic_designer', 'Graphic Designer'),
        ('motion_designer', 'Motion Designer'),
        ('3d_designer', '3D Designer'),
        ('product_manager', 'Product Manager'),
        ('cto', 'Chief Technology Officer'),
        ('business_analyst', 'Business Analyst'),
        ('data_analyst', 'Data Analyst'),
        ('data_scientist', 'Data Scientist'),
        ('data_analyst', 'Data Analyst'),
        ('system_analyst', 'System Analyst'),
        ('system_administrator', 'System Administrator'),
        ('network_engineer', 'Network Engineer'),
        ('sup_engineer', 'Support Engineer'),
        ('dba', 'Database Administrator'),
        ('sales_manager', 'Sales Manager'),
        ('marketing_specialist', 'Marketing Specialist'),
        ('acc_manager', 'Account Manager'),
        ('recruiter', 'Recruiter'),
        ('ceo', 'CEO'),
        ('employer', 'Employer')


    ]
    roles = models.CharField(max_length=50, default='employer', choices=ROLE_CHOICES)
    spaces_count = models.IntegerField(default=0)

    def __str__(self):
        """
        Return a string representation of this user.

        This is the username, which is guaranteed to be unique for all users.
        """

        return self.username





        







    