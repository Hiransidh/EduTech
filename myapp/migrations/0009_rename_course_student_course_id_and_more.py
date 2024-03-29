# Generated by Django 4.2.5 on 2024-03-28 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_student_batch_id_student_branch_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='course_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='branch',
        ),
        migrations.AddField(
            model_name='student',
            name='branch_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.branch'),
            preserve_default=False,
        ),
    ]