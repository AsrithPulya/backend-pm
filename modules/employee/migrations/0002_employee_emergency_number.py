# Generated by Django 5.1.3 on 2024-12-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emergency_number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
