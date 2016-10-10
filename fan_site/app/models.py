from django.db import models

class House(models.Model):
    name = models.CharField(max_length = 40)
    symbol = models.CharField(max_length = 40)
    color = models.CharField(max_length = 40)
    motto = models.CharField(max_length = 40)
    leader = models.CharField(max_length = 40)
    rival = models.ForeignKey("self", null=True, blank=True)
    img = models.CharField(max_length = 300, default =1)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length = 50)
    leader = models.ForeignKey(House)
    capital = models.CharField(max_length = 40)
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
