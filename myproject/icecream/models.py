from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    email = models.CharField(max_length=60)
    job = models.CharField(max_length=30)

class Child(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    parent_id = models.ForeignKey("Parent", on_delete=models.CASCADE)
