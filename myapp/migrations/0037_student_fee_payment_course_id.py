# Generated by Django 4.2.5 on 2024-04-15 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_remove_student_fee_payment_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_fee_payment',
            name='course_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='myapp.course'),
            preserve_default=False,
        ),
    ]
