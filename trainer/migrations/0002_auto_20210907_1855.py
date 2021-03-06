# Generated by Django 3.2.4 on 2021-09-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='company',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='course',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='days',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='identification_card',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='job_title',
            field=models.CharField(max_length=20),
        ),
    ]
