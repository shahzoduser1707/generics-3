from django.db import models
from datetime import datetime
# Create your models here.

class LaptopModel(models.Model):
    name = models.CharField(max_length=200,default='')
    created_at = models.DateTimeField(default=datetime.now)
    function = models.CharField(max_length=200,default='')
    price = models.IntegerField(default=0)
    desc = models.TextField(default='write smth pls!')

    class Meta:
        db_table = 'LaptopModel'
    def __str__(self) -> str:
        return self.name