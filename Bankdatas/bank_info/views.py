from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Banks
from .serializers import BanksSerializer


  
class Bank_ifsc(generics.ListCreateAPIView): 
    # permission_classes = (IsAuthenticated,) 

    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    def get(self, request, ifsc):
        bank_ifsc = Banks.objects.get(ifsc=ifsc)
        return Response(BanksSerializer(bank_ifsc).data)    


 
class Bank_branch(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,) 

    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    def get(self, request, bank_name, city):
        bank_details = Banks.objects.filter(
            bank_name__icontains = bank_name,
            city__iexact = city
        )
        serializer = BanksSerializer(bank_details, many=True)
        return Response(serializer.data)

