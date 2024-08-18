from rest_framework import serializers
from scts.models import Student, Classroom


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'age']


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'age']

    def get_id(self, obj):
        return obj.id


class ClassroomSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Classroom
        fields = ['id', 'classroom_name']
    def get_id(self, obj):
        return obj.id
