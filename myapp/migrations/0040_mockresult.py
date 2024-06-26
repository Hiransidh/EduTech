# Generated by Django 4.2.5 on 2024-04-16 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_mock_question_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='mockresult',
            fields=[
                ('test_id', models.IntegerField(primary_key=True, serialize=False)),
                ('impression', models.CharField(max_length=90)),
                ('date', models.DateField(max_length=90)),
                ('time', models.CharField(max_length=90)),
                ('status', models.CharField(max_length=90)),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
            options={
                'db_table': 'mockresult',
            },
        ),
    ]
