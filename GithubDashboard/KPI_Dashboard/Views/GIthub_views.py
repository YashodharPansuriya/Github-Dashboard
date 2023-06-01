# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse
# from KPI_Dashboard.serializers import Github_issueSerializer
import requests
# Create your views here.
from KPI_Dashboard.models import Github_issue


def featch_issue_store_data(request):
    api_url = 'https://api.github.com/repos/YashodharPansuriya/Github-Dashboard/issues'
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"  # Add additional headers as required
    }
    response = requests.get(api_url, headers=headers)
    data = response.json()
    items = []
    for item in data:
        github_issue = Github_issue(
                issue_number=item['number'],
                title=item['title'],
                body=item['body'],
                created_at=item['created_at'],
                updated_at=item['updated_at'],
                state=item['state'],
                assignee=item['assignee']['login']
            )
        github_issue.save()
            
        # print(items[i]['number'], end="\n")
        # print(items[i]['title'], end="\n")
    return HttpResponse("Data fetched and stored successfully.")
    

  
    









# @csrf_exempt
# def github_issue(request, id=0):
    # if request.method == 'GET':
    #     github_issue = Github_issue.objects.all()
    #     github_issue_Serializer = Github_issueSerializer(github_issue, many=True) #using this we convert data to json format
    #     return JsonResponse(github_issue_Serializer.data, safe=False)
    # elif request.method == 'POST':
    #     github_issue_data = JSONParser().parse(request)
    #     github_issue_Serializer = Github_issueSerializer(data=github_issue_data) #using this we convert jason formate to model data
    #     if github_issue_Serializer.is_valid():
    #         github_issue_Serializer.save()
    #         return JsonResponse("Added Successfully", safe=False)
    #     return JsonResponse("Failed to Add", safe=False)
    # elif request.method == 'PUT':
    #     github_issue_data = JSONParser().parse(request)
    #     github_issue = Github_issue.objects.get(issueId = github_issue_data['issueId'])
    #     github_issue_Serializer = Github_issueSerializer(github_issue, data=github_issue_data) #using this we convert jason formate to model data
    #     if github_issue_Serializer.is_valid():
    #         github_issue_Serializer.save()
    #         return JsonResponse("Updated Successfully", safe=False)
    #     return JsonResponse("Failed to Update", safe=False)
    # elif request.method == 'DELETE':
    #     github_issue = Github_issue.objects.get(issueId = id)
    #     github_issue.delete()
    #     return JsonResponse("Deleted Successfully", safe=False)
    


