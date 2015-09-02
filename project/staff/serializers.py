from rest_framework.serializers import ModelSerializer
from .models import Staff, Vacancy


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        depth = 1

class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        depth = 1