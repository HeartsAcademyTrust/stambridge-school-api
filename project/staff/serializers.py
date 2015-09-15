from rest_framework.serializers import ModelSerializer
from .models import Staff, Vacancy, Department


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        depth = 1
        fields = ('name', 'role', 'photo', 'extra_info')

class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        depth = 1

class DepartmentSerializer(ModelSerializer):
    staff = StaffSerializer(many=True, read_only=True)
    vacancies = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('name', 'school', 'staff', 'vacancies')
        depth = 1;