# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Api(models.Model):
    api_name = models.CharField(max_length=255, primary_key=True)
    class_field = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'API'


class ApiSpecific(models.Model):
    general = models.CharField(primary_key=True, max_length=255)
    specific = models.CharField(max_length=255)
    api_name_fk = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'API_specific'

    def __str__(self):
        return self.general


class ApiSpecificBackup(models.Model):
    general = models.CharField(max_length=255)
    specific = models.CharField(max_length=255)
    api_name_fk = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'API_specific_backup'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class File(models.Model):
    file_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    project = models.CharField(max_length=255)

    class Meta:
        db_table = 'file'


class FileApi(models.Model):
    file_name = models.CharField(max_length=255)
    api_name = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = 'file_API'


class Project(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    dir_trab = models.CharField(max_length=255)
    language = models.CharField(max_length=255)

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.name

class UserSkill(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(primary_key=True)
    skill = models.TextField(blank=True)
    
    class Meta:
        db_table = 'matchsource_userskill'

    def __str__(self):
        return self.name + ' - ' + self.email + ' - ' + self.skill

class GitHub(models.Model):
    github = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'githubusername'


class Skills(models.Model):
    file = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, primary_key=True)
    class_name = models.CharField(max_length=255)
    ref_count = models.IntegerField(blank=True)
    
    class Meta:
        db_table = 'skillss'
