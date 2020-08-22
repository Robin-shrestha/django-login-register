from django.shortcuts import render
from .serializer import ParadigmSerializer, LanguageSerializer, ProgrammerSerializer
from .models import Paradigm, Language, Programmers
from rest_framework import viewsets, permissions
# Create your views here.

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmers.objects.all()
    serializer_class = ProgrammerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    