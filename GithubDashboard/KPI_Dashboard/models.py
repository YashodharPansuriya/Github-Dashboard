from django.db import models

# Create your models here.

class Github_issue(models.Model):
    issue_number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=2000)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    state = models.CharField(max_length=100)
    assignee = models.CharField(max_length=2000)
    
