from rest_framework import serializers
from .models import Auther,Books


class Books_Serializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Books
        fields =["id","auther_name_s","book_name"]

    



class Auther_Serializer(serializers.ModelSerializer):
    books = Books_Serializer(many=True,source='auther_model')

    class Meta: 
        model = Auther
        fields =["id","auther_name","books"]

    def create(self, validated_data):
        auther_name = validated_data.pop('auther_model')
        authers = Auther.objects.create(**validated_data)
        for event in auther_name:
            Books.objects.create(auther_name_s_id=authers.id, **event) 
        return authers
    

    def update(self, instance, validated_data):
        books_data = validated_data.pop('auther_model')
        books = (instance.auther_model).all()
        books = list(books)
        instance.auther_name = validated_data.get('auther_name', instance.auther_name)
        instance.save()
        for book_data in books_data:
            book = books.pop(0)
            book.book_name = book_data.get('book_name', book.book_name)
            book.save()
        return instance
          