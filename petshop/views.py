from rest_framework import viewsets
from petshop.models import Animal, Services 
from petshop.serializers import AnimalSerializers, ServicesSerializers

class AnimalViewSets (viewsets.ModelViewSet):
    queryset = Animal.objects.all ()
    serializer_class = AnimalSerializers

class ServicesViewSets (viewsets.ModelViewSet):
    queryset = Services.objects.all ()
    serializer_class = ServicesSerializers






# Create your views here.
