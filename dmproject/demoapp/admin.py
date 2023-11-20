from django.contrib import admin

from . models import service
from . models import team

# Register your models here.
admin.site.register(service)
admin.site.register(team)