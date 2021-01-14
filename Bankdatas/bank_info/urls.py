from django.urls import path,include
from . import views 
  
urlpatterns = [ 
    path('api/<str:ifsc>/', views.BankIfsc.as_view(), name ='Bank Ifsc'), 
    path('api/<str:bank_name>/<str:city>/', views.BankBranch.as_view(), name ='Bank Branch'), 
    path('api/',include('rest_framework.urls', namespace = 'rest_framework'))


] 
