from django.contrib.auth.models import User, Group
from models import Employees
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('url','emp_no','birth_date','to_date','first_name', 'last_name' , 'gender','hire_date','dept_emp_from_date','dept_emp_departments_dept_no')
