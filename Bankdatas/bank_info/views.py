from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.permissions import IsAuthenticated
from .models import Banks
from .serializers import BanksSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets

from .pagination import CustomNumberPagination



# This BankBranch is for fetching the details of the branches with given bank_name and city
  
class BankBranch(generics.ListAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    pagination_class = LimitOffsetPagination
    


    def get(self, request, bank_name, city):
       queryset = Banks.objects.filter(city__iexact=city, bank_name__icontains=bank_name)
       page = self.paginate_queryset(queryset)
       if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

       serializer = self.get_serializer(queryset, many=True)
       return Response(serializer.data)


# This Bankranch Class is for fetching the bank details of given ifsc code
class BankIfsc(generics.ListAPIView): 
    permission_classes = (IsAuthenticated,) 
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    def get(self, request, *args, **kwargs):
        try:
            bank = self.queryset.get(ifsc=kwargs["ifsc"])
            return Response(BanksSerializer(bank).data) 
        except Banks.DoesNotExist:
            return Response(data={"message": "Bank with ifsc does not exist"},status=status.HTTP_404_NOT_FOUND)



 


