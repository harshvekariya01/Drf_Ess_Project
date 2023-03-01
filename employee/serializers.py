from rest_framework import serializers
from .models import Employee,designation,department,leave_type,leave,attendence



class Empoloyee_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields =["id","username","first_name","last_name","email","dob","phone_no","email","employee_designation","employee_department","acess_type"]

class Designation_Serializer(serializers.ModelSerializer):

    class Meta:
        model = designation
        fields =["designation_name","tracks"]

class Department_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = department
        fields ="__all__"
  
class Leave_type_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = leave_type
        fields ="__all__"

class Leave_Serializer(serializers.ModelSerializer):
    class Meta:
        model = leave
        fields ="__all__"

class Attendence_Serializer(serializers.ModelSerializer):
    class Meta:
        model = attendence
        fields ="__all__"

class Approved_reject_Serializer(serializers.ModelSerializer):
    class Meta:
        model = leave
        fields =["employee_name","start_date","end_date","leave_types","status","A_R_date"]


class Punch_in_out_Serializer(serializers.ModelSerializer):
    class Meta:
        model = attendence
        fields ="__all__"


class Change_password_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        


