from django.shortcuts import render

# Create your views here.
from .models import Auther,Books
from drf_test.serializers import Auther_Serializer,Books_Serializer 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response



class Auther_viewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Auther_Serializer
    queryset =  Auther.objects.all()
    lookup_field = "id"
    


    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     print(data,'=============================')
    #     authers = Auther.objects.create(auther_name=data['auther_name'],)
    #     books = Books.objects.create(book_name=data['book_name'],auther_name_s=authers)
    #     serializer = Auther_Serializer(authers)
    #     return Response(serializer.data) 



class Books_viewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Books_Serializer
    queryset =  Books.objects.all()
    lookup_field = "id"



