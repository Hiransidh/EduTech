# Generated by Django 4.2.5 on 2024-04-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_alter_staff_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='subject',
            field=models.CharField(max_length=15),
        ),
    ]
