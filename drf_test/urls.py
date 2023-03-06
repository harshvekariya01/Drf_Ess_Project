from django.urls import path
from . import views
from knox import views as knox_views

app_name = "drf_test"

urlpatterns = [
    
    
    path('Auther_viewset/',views.Auther_viewset.as_view({'get':'list','post':'create'})),
    path('Auther_viewset/<id>',views.Auther_viewset.as_view({'get':'retrieve','put':'update',})),
    path('Auther_viewset/<id>',views.Auther_viewset.as_view({'delete':'destroy'})),



    


    
    path('Books_viewset/',views.Books_viewset.as_view({'get':'list','post':'create'})),
    path('Books_viewset/<id>',views.Books_viewset.as_view({'get':'retrieve','put':'update','delete':'destroy'})),




]