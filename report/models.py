from django.db import models
from django_jalali.db import models as jmodels

class Region(models.Model):

    name = models.CharField(max_length=40)
    code = models.IntegerField()
    def __str__(self):
        return self.name

class Data(models.Model):

    date = jmodels.jDateField()
    region = models.ForeignKey(Region,on_delete=models.SET_NULL,null=True)
    loaded_boxes = models.PositiveIntegerField()
    returned_boxes = models.PositiveIntegerField(default=0)
    check1 = models.BooleanField(default=False)
    check2 = models.BooleanField(default=False)

    def __str__(self):
        return self.region.name
