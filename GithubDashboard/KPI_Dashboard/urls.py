from django.urls import path
from KPI_Dashboard.Views.Github_views import github_issue

urlpatterns = [
   path('github_issue/', github_issue, name='github_issue'),
#    path('github_issue/([0-9]+)', github_issue, name='github_issue'),
   path('github_issue/<int:id>/', github_issue),
]