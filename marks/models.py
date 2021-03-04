from django.db import models

# Create your models here.
class Marks(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.IntegerField()
    math = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    total = models.IntegerField()
    per = models.FloatField()