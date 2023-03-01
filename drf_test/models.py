from django.db import models



class employee(models.Model):
    emp_id = models.CharField(max_length=100)
    emp_name = models.CharField(max_length=255)
    emp_email = models.EmailField(max_length=255, unique=True)