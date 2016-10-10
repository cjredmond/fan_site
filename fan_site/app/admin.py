from django.contrib import admin

# Register your models here.
from app.models import House, Region

admin.site.register(House)
admin.site.register(Region)
