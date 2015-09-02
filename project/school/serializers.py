from rest_framework.serializers import ModelSerializer
from .models import SchoolMenu, Newsletter, Policy


class SchoolMenuSerializer(ModelSerializer):
    class Meta:
        model = SchoolMenu
        depth = 1

class SchoolNewslettersSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        depth = 1

class SchoolPoliciesSerializer(ModelSerializer):
    class Meta:
        model = Policy
        depth = 1