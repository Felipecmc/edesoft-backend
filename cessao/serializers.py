from rest_framework import serializers

from cessao.models import Cessao

class CessaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cessao 
        fields = '__all__'
        


class Dataserializer(serializers.Serializer):
    bucket_name = serializers.CharField()
    object_key = serializers.CharField()