from rest_framework import serializers
from . import models
class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Paradigm
        fields = '__all__'

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Language
        fields = '__all__'

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Programmers
        fields =['id', 'url', 'name', 'age', 'language']

