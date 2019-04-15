# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employees(models.Model):
	emp_no = models.IntegerField()
	birth_date = models.DateField()
	to_date = models.DateField()
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	gender = models.CharField(max_length=45)
	hire_date = models.DateField()
	dept_emp_from_date= models.DateField()
	dept_emp_departments_dept_no = models.CharField(max_length=45)
	
	class Meta:
		managed=False
		db_table ='employees'