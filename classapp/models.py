from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=30,default='No Name Provided')
    address=models.TextField(max_length=200)
    email=models.TextField(max_length=100)

    class Meta:
        managed=True
        db_table='Teacher'

class Student(models.Model):
    student_id=models.PositiveIntegerField(primary_key= True)
    name=models.TextField(max_length=100)
    form=models.IntegerField()
    Class=models.CharField(max_length=5)
    image=models.ImageField(upload_to="profilepic/",default="profilepic/avatar.jpg")
    GPA=models.FloatField()
    address=models.TextField(max_length=100)
    discipleRecord=models.TextField(max_length=100)
    feedback=models.TextField(max_length=100)
    modules=models.TextField(max_length=300,default=" ")

    class Meta:
        managed= True
        db_table= 'Student'

# class Modules(models.Model):
#     student=models.ForeignKey(Student,on_delete=models.CASCADE,primary_key=True)
#     modules=models.TextField()
#
#     class Meta:
#         managed= True
#         db_table='Modules'

class Attendance(models.Model):
    attendance_id=models.AutoField(primary_key=True)
    status=models.TextField(max_length=10)
    studentname=models.TextField(max_length=100,default="No Name")
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    attDate=models.DateTimeField(default=timezone.now,blank=False)
    comments=models.TextField(max_length=200, default=" ")



    class Meta:
        managed=True
        db_table= 'Attendance'






# class Enquiry(models.Model):
#     who=models.CharField(max_length=100)
#     orderText=models.CharField(max_length=100)
#     leadTime=models.CharField(max_length=100)
#     enquiryId=models.AutoField(primary_key=True)
#     timeofEnquiry=models.DateTimeField(default=datetime.now,blank=False)
#
#     class Meta:
#         managed = True
#         db_table = 'Enquiry'

# class Enquiry(models.Model):
#     who=models.CharField(max_length=100)
#     orderText=models.CharField(max_length=100)
#     leadTime=models.CharField(max_length=100)
#     enquiryId=models.AutoField(primary_key=True)
#     timeofEnquiry=models.DateTimeField(default=datetime.now,blank=False)
#
#     class Meta:
#         managed = True
#         db_table = 'Enquiry'