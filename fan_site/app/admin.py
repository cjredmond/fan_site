from django.contrib import admin

# Register your models here.
from app.models import House, Region, SmallHouse

admin.site.register(House)
admin.site.register(Region)
admin.site.register(SmallHouse)
