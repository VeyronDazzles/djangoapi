#This is a Serializer
#Added Fields and model

from rest_framework import serializers
from .models import course

class courseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = course
        fields = ('id','url','name','language','price')
