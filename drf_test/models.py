from django.db import models



class Auther(models.Model):
    auther_name = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.auther_name





class Books(models.Model):
    auther_name_s = models.ForeignKey(Auther,on_delete=models.CASCADE,blank=True,null=True,related_name="auther_model")
    book_name = models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.book_name

    