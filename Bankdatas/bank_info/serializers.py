from rest_framework import serializers

from .models import Banks

class BanksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banks
        fields = '__all__'