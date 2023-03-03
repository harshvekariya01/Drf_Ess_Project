from datetime import date, datetime
from pytz import timezone
from django.shortcuts import render,redirect
from .models import  department, designation,leave_type,leave,attendence
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,logout
from django.contrib import messages 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Employee
from rest_framework import filters

# -------------------------API--------------------------------
from employee.serializers import (Empoloyee_Serializer,Designation_Serializer,Department_Serializer,Leave_type_Serializer,
                                Leave_Serializer,Attendence_Serializer,Approved_reject_Serializer,Punch_in_out_Serializer,
                                Change_password_Serializer
                                )
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets
from rest_framework import permissions
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

# -------------------------API Class----------------------------
class login_viewset(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
            print("Login-----------------------------",self)
            print('request.data---------------------------',request.data)
            serializer = AuthTokenSerializer(data = request.data)
            serializer.is_valid()
            user = serializer.validated_data['user']
            login(request,user)
            list = super(login_viewset,self).post(request)
            print("Token---------------------------------------",  list.data)

            list.data['Username'] = user.first_name
            list.data['Email'] = user.email

            return Response(list.data)
    
class Employee_viewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Empoloyee_Serializer
    queryset =  Employee.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^username','email']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['email']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']
    

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data,'=============================')
        users = Employee.objects.create(username=data['username'],first_name=data['first_name'],last_name=data['last_name'],
                                        email=data['email'],dob=data['dob'],address=data['address'],phone_no=data['phone_no']
                                          ,employee_designation_id=data['employee_designation_id'],employee_department_id=
                                          data['employee_department_id'],acess_type=data['acess_type'],
                                          )
        users.password=make_password(password=data['password'])
        users.save()
        serializer = self.serializer_class(users)
        return Response(serializer.data)       

class Designation_viewset(viewsets.ModelViewSet):       
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Designation_Serializer
    queryset =  designation.objects.all()

class Department_viewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Department_Serializer
    queryset =  department.objects.all()

class Leave_type_viewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Leave_type_Serializer
    queryset =  leave_type.objects.all()      

class Leave_viewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Leave_Serializer
    lookup_field ="id"
    queryset =  leave.objects.all()      

class Attendence_viewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Attendence_Serializer
    queryset =  attendence.objects.all()     

class Approved_reject_viewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Approved_reject_Serializer
    lookup_field ="id"

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['id']
        queryset =  leave.objects.get(employee_name__id=self.kwargs['id'])
        serializer = Approved_reject_Serializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        if request.data['status'] == 'Approved':
            print('----------------------',request.data,self.kwargs['id'])
            statu = leave.objects.get(employee_name__id=self.kwargs['id'])
            statu.status = 'Approved successfully'
            statu.A_R_date=date.today()
            statu.save()
            return Response(data={'success'})
        

        if request.data['status'] == 'Rejected':
            print('----------------------',request.data)
            status = leave.objects.filter(employee_name__id=self.kwargs['id']).update(
            status = 'Rejected')
            return Response(data={'Rejected successfully'})
    
class Punch_in_out_viewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Punch_in_out_Serializer
    queryset =  attendence.objects.all() 

    def create(self, request, *args, **kwargs):
        if request.data['status'] == 'punchin':
            status = attendence.objects.create(
                employee_name_id=request.user.id,date = date.today(),
                punch_in=datetime.now(timezone("Asia/Kolkata")))
            return Response(data={'punch-in successfully'})
        if request.data['status'] == 'punchout':
            status = attendence.objects.get(employee_name_id=request.user.id,punch_out=None)
            status.punch_out = datetime.now(timezone("Asia/Kolkata"))
            status.date = date.today()
            print(status.punch_out , status.punch_in,'=================================')
            print(status.punch_out-status.punch_in,'=================================')

            status.duration = status.punch_out - status.punch_in
            status.save()
            return Response(data={'punch-out successfully'})
    
    
class Change_password_viewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Change_password_Serializer
    queryset =  Employee.objects.all() 

    def update(self, request, *args, **kwargs):
        oldpassword = request.data['oldpassword']
        newpassword = request.data['newpassword']
        confirmpassword = request.data['confirmpassword']
        user = Employee.objects.get(email=request.user.email)
        if not user.check_password(oldpassword):
            return Response({"message":"old password is not correct"},status=status.HTTP_200_OK)
        else:
            if newpassword==confirmpassword:
                user = Employee.objects.get(id=request.user.id)
                user.password = make_password(password=confirmpassword)
                user.save()
                return Response({"message":"change password sucessfully"},status=status.HTTP_200_OK)
            else:
                return Response({"error":"newpassword and confirmpassword are not same"},status=status.HTTP_400_BAD_REQUEST)
        






    








