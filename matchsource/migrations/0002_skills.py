# Generated by Django 3.0.3 on 2020-02-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchsource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('file', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=255)),
                ('ref_count', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'skillss',
            },
        ),
    ]