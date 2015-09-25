from rest_framework.serializers import ModelSerializer
from .models import SchoolMenu, SchoolYear, StatutoryInfo, SchoolLetters, Newsletter, Policy


class SchoolMenuSerializer(ModelSerializer):
    class Meta:
        model = SchoolMenu
        depth = 1

class SchoolLettersSerializer(ModelSerializer):
    class Meta:
        model = SchoolLetters
        depth = 1
        fields = ('title', 'description', 'deadline', 'file')

class SchoolYearSerializer(ModelSerializer):
    letters = SchoolLettersSerializer(many=True, read_only=True)

    class Meta:
        model = SchoolYear
        fields = ('year', 'school', 'letters')
        depth = 1;

class SchoolNewslettersSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        depth = 1

class SchoolPoliciesSerializer(ModelSerializer):
    class Meta:
        model = Policy
        depth = 1

class SchoolStatutoryInfoSerializer(ModelSerializer):
		class Meta:
				model = StatutoryInfo
				depth = 1