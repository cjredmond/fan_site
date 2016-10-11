from django.db import models

class Info(models.Model):
    name = models.CharField(max_length = 40)
    symbol = models.CharField(max_length = 40)
    color = models.CharField(max_length = 40)
    motto = models.CharField(max_length = 40)
    leader = models.CharField(max_length = 40)
    rival = models.ForeignKey("self", null=True, blank=True)
    img = models.CharField(max_length = 300, default =1)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True



class House(Info):
    name = models.CharField(max_length = 50)


class Region(models.Model):
    name = models.CharField(max_length = 50)
    leader = models.ForeignKey(House)
    capital = models.CharField(max_length = 40)
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class SmallHouse(Info):
    name = models.CharField(max_length = 45)
    region = models.ForeignKey(Region, null=True, blank=True)
    capital = models.CharField(max_length = 45, default = "a")
