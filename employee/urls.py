from django.urls import path
from . import views
from knox import views as knox_views

app_name = "employee"

urlpatterns = [
    
    path('login_viewset/',views.login_viewset.as_view()), 

    path('LogoutView/',knox_views.LogoutView.as_view()),

    path('Employee_viewset/',views.Employee_viewset.as_view({'get':'list','post':'create'})),

    path('Designation_viewset/',views.Designation_viewset.as_view({'get':'list','post':'create'})),

    path('Department_viewset/',views.Department_viewset.as_view({'get':'list','post':'create'})),

    path('Leave_type_viewset/',views.Leave_type_viewset.as_view({'get':'list','post':'create'})),

    path('Leave_viewset/',views.Leave_viewset.as_view({'get':'list','post':'create','delete':'destroy'})),   

    path('attendence_viewset/',views.Attendence_viewset.as_view({'get':'list','post':'create'})), 

    path('approved_reject_viewset/<id>',views.Approved_reject_viewset.as_view({'get':'retrieve','patch':'update'})),

    path('Punch_in_out_viewset/',views.Punch_in_out_viewset.as_view({'post':'create'})), 

    path('Change_password_viewset/',views.Change_password_viewset.as_view({'post':'update','get':'list'})),  



]





