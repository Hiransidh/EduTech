# Generated by Django 4.2.5 on 2024-04-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_staff_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
    ]
