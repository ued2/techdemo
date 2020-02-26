from django.contrib import admin
from django.db import models
from .models import UserSkill


class UserSkillAdmin(admin.ModelAdmin):
    model = UserSkill
    list_display = ('name', 'email', 'skill')


admin.site.register(UserSkill, UserSkillAdmin)
