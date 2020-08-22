from django.db import models

# Create your models here.
class Paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programmers(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    language = models.ManyToManyField(Language)

    def __str__(self):
        return f"({self.name}, {self.age})"