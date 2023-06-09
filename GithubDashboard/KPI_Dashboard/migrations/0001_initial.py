# Generated by Django 4.0.5 on 2023-05-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Github_issue',
            fields=[
                ('issueId', models.AutoField(primary_key=True, serialize=False)),
                ('issue_number', models.IntegerField()),
                ('title', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('state', models.CharField(max_length=100)),
                ('assignee', models.CharField(max_length=2000)),
            ],
        ),
    ]
