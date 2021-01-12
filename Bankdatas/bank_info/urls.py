from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path('api/<str:ifsc>', views.Bank_ifsc.as_view(), name ='Bank Ifsc'), 
    path('api/<str:bank_name>/<str:city>', views.Bank_branch.as_view(), name ='Bank Ifsc'), 


] 