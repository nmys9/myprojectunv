from django.db import models

# Create your models here.

class Course(models.Model):
    course_id=models.PositiveIntegerField(primary_key=True,unique=True)
    course_name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

# class Location(models.Model):
#     location_id=models.AutoField(primary_key=True)
#     building=models.CharField(max_length=200)
#     room=models.CharField(max_length=200)
    
#     def __str__(self):
#         return f'{self.building}, {self.room}'
    
# class Professor(models.Model):
#     professor_id=models.AutoField(primary_key=True)
#     professor_name=models.CharField(max_length=200)
    

# class Student(models.Model):
#     student_id=models.PositiveIntegerField(primary_key=True)
#     student_name=models.CharField(max_length=200)
    

# class Lecture(models.Model):
#     lecture_id=models.AutoField(primary_key=True)
#     course=models.ForeignKey(Course,on_delete=models.CASCADE)
#     section=models.IntegerField(auto_created=1)
#     day=models.DateField()
#     time=models.DateTimeField()
#     location=models.ForeignKey(Location,on_delete=models.CASCADE)
#     professor=models.ForeignKey(Professor,on_delete=models.CASCADE)
    
    
class WiFiFingerprint(models.Model):
    ssid=models.CharField(max_length=100)
    bssid=models.CharField(max_length=50,null=True)
    rssi_min=models.IntegerField()
    rssi_max=models.IntegerField()
    location_name=models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.ssid} {self.location_name}"
    