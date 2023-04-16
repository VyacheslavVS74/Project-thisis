from django.db import models


class Works(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', null=True, blank=True)
    top_sales = models.ManyToManyField('Top', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    material = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Top(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
