from django.db import models


class NamePeople(models.Model):

    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name

class PhysicalCharac(models.Model):

    namePeople = models.ForeignKey(NamePeople, on_delete=models.CASCADE, null=True)
    height = models.CharField(max_length=10)
    mass = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.height
