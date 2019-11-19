from django.contrib import admin
from django.db import models
from .models import UserSkill, SocialAuthUsersocialauth


class UserSkillAdmin(admin.ModelAdmin):
    model = UserSkill
    list_display = ('name', 'email', 'skill')


class GitHubAdmin(admin.ModelAdmin):
    model = SocialAuthUsersocialauth
    list_display = ('user', 'extra_data', 'provider')


admin.site.register(UserSkill, UserSkillAdmin)
admin.site.register(SocialAuthUsersocialauth, GitHubAdmin)
