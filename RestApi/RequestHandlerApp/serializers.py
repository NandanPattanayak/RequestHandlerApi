from rest_framework import serializers
from .models import demoModels,demo2Model
class demoModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = demoModels
        fields = '__all__'

class demo2ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = demo2Model
        fields = '__all__'