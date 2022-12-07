from rest_framework import serializers

from cessao.models import Cessao

class CessaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cessao 
        fields = '__all__'