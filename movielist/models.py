from django.db import models

# Create your models here.

class Record(models.Model):
    title=models.CharField(max_length=100)
    memo=models.TextField(blank=True,null=True)
    rate=models.IntegerField(choices=[(0,"☆☆☆☆☆"),(1,"★☆☆☆☆"),(2,"★★☆☆☆"),(3,"★★★☆☆"),(4,"★★★★☆"),(5,"★★★★★")])
    kinds=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.title