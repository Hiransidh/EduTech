# Generated by Django 4.2.5 on 2024-03-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_result_test_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='eligibility',
            name='status',
            field=models.CharField(default='pending', max_length=100),
            preserve_default=False,
        ),
    ]
