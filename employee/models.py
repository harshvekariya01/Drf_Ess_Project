from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.db import models 


class designation(models.Model):
    designation_name = models.CharField(max_length=100)

    def __str__(self):
        return self.designation_name
    
class department(models.Model):
    department_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class Employee(AbstractUser):
    username =  models.CharField(max_length=250,blank=True,null=True,unique=True)
    first_name =  models.CharField(max_length=250,blank=True,null=True)
    last_name =  models.CharField(max_length=250,blank=True,null=True)
    email = models.EmailField(blank=True)
    dob = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    phone_no = models.BigIntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True,unique=True)
    password = models.CharField(max_length=12)
    employee_designation = models.ForeignKey(designation,on_delete=models.CASCADE,blank=True,null=True)
    employee_department = models.ForeignKey(department,on_delete=models.CASCADE,blank=True,null=True)
    access_status = (
        ('A','Admin'),
        ('E','Employee')
    )
    acess_type = models.CharField(max_length=20,choices=access_status,blank=True,null=True)

    
    
    def __str__(self):
        return self.first_name

class leave_type(models.Model):
    leave_name = models.CharField(max_length=100)
    max_leaves = models.IntegerField()
    CARRY_STATUS = (
        ('Yes','Yes'),
        ('No','No')
    ) 
    carry_forword = models.CharField(max_length=20,choices=CARRY_STATUS)

    def __str__(self):
        return self.leave_name

class leave(models.Model):
    employee_name = models.ForeignKey(Employee,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_types = models.ForeignKey(leave_type,on_delete=models.CASCADE)
    LEAVE_STATUS = (
        ('Approved','Approved'),
        ('Rejected','Rejected')
    ) 
    status = models.CharField(max_length=20,choices=LEAVE_STATUS,blank=True,null=True)
    A_R_date  = models.DateField(blank=True,null=True)

    # def __str__(self):
    #     return self.employee_name.first_name
    


class attendence(models.Model):
    employee_name =  models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True,related_name='employee_attendence')
    punch_in = models.DateTimeField(null=True,blank=True)
    punch_out = models.DateTimeField(null=True,blank=True)
    date =  models.DateField()
    duration = models.CharField(max_length=200,blank=True,null=True,default=0)

    
    
