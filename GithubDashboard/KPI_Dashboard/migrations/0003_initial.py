# Generated by Django 4.0.5 on 2023-05-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('KPI_Dashboard', '0002_delete_github_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Github_issue',
            fields=[
                ('issueId', models.AutoField(primary_key=True, serialize=False)),
                ('issue_number', models.IntegerField()),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=100)),
                ('assignee', models.CharField(max_length=500)),
            ],
        ),
    ]
