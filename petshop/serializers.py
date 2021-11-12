from rest_framework import serializers
from petshop.models import Animal, Services

class AnimalSerializers (serializers.ModelSerializer):
    class Meta ():
        model= Animal
        fields= '__all__'


class ServicesSerializers (serializers.ModelSerializer):
    class Meta ():
        model= Services
        fields= '__all__'