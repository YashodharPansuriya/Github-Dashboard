from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from KPI_Dashboard.models import Github_issue
from KPI_Dashboard.serializers import Github_issueSerializer
# Create your views here.

@csrf_exempt
def github_issue(request, id=0):
    if request.method == 'GET':
        github_issue = Github_issue.objects.all()
        github_issue_Serializer = Github_issueSerializer(github_issue, many=True) #using this we convert data to json format
        return JsonResponse(github_issue_Serializer.data, safe=False)
    elif request.method == 'POST':
        github_issue_data = JSONParser().parse(request)
        github_issue_Serializer = Github_issueSerializer(data=github_issue_data) #using this we convert jason formate to model data
        if github_issue_Serializer.is_valid():
            github_issue_Serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        github_issue_data = JSONParser().parse(request)
        github_issue = Github_issue.objects.get(issueId = github_issue_data['issueId'])
        github_issue_Serializer = Github_issueSerializer(github_issue, data=github_issue_data) #using this we convert jason formate to model data
        if github_issue_Serializer.is_valid():
            github_issue_Serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        github_issue = Github_issue.objects.get(issueId = id)
        github_issue.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    


