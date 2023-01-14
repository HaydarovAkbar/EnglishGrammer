from django.shortcuts import render
from .serializers import Grammer, GrammerSerializers
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class GrammerViews(ModelViewSet):
    queryset = Grammer.objects.all()
    serializer_class = GrammerSerializers
