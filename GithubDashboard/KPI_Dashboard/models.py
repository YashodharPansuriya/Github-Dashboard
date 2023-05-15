from django.db import models

# Create your models here.

class Github_issue(models.Model):
    issueId = models.AutoField(primary_key=True)
    issue_number = models.IntegerField()
    title = models.CharField(max_length=500)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    state = models.CharField(max_length=100)
    assignee = models.CharField(max_length=500)
    
