from django.urls import path
from KPI_Dashboard.Views.Github_views import featch_issue_store_data

urlpatterns = [
    path('', featch_issue_store_data)
   # path('github_issue/', github_issue, name='github_issue'),
   # path('github_issue/<int:id>/', github_issue),
]