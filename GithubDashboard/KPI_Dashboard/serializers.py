from rest_framework import serializers
from KPI_Dashboard.models import Github_issue

class Github_issueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Github_issue
        fields = '__all__'