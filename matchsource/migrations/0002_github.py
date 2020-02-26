# Generated by Django 3.0.3 on 2020-02-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchsource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitHub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=255)),
                ('github', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'githubusername',
            },
        ),
    ]
