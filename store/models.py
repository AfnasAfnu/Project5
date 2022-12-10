from django.db import models

# Create your models here.

class Departments(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Courses(models.Model):
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class Person(models.Model):
    name = models.CharField(max_length=124)
    email = models.EmailField(max_length=125)
    DOB = models.DateField(max_length=8,null=True)
    Age = models.IntegerField(null=True)
    Mobile_Number = models.IntegerField(null=True)
    gen_cho = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))
    gender = models.TextField(choices=gen_cho)
    Address = models.CharField("Address",max_length=500)
    pin_code = models.CharField("Pincode",max_length=6)
    departments = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    courses = models.ForeignKey(Courses, on_delete=models.SET_NULL,null=True)
    use = (('Enquiry', 'Enquiry'), ('Place Order','Place Order'), ('Return ', 'Return '),('Replacement','Replacement'))
    purpose = models.TextField(choices=use,null=True)

    def __str__(self):
        return self.name
