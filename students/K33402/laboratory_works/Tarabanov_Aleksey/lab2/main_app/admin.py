from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Race)
admin.site.register(models.Register)
admin.site.register(models.Comment)
