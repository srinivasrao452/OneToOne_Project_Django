
from django.db import models

# Creating Student Model Code
class Student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return self.sname

class Course(models.Model):
    cno = models.IntegerField()
    cname = models.CharField(max_length=50)
    cfee = models.IntegerField()

    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.cname



class Person(models.Model):
    sno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



'''
class Sample(models.Model):
    xyz = models.SmallIntegerField() # 10000
    xyz = models.IntegerField() # 10000
    mobile = models.BigIntegerField(unique=True, blank=True,null=True) # 10000

    xyz = models.FloatField() # 10000.00
    xyz = models.DecimalField(max_digits=10, decimal_places=3) # 10000.000

    xyz = models.CharField(max_length=50)
    xyz = models.TextField()

    xyz = models.OneToOneField(max_length=50)
    xyz = models.ForeignKey(max_length=50)
    xyz = models.ManyToManyField(max_length=50)

    xyz = models.ImageField()
    xyz = models.FileField()
'''












