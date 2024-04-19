# Generated by Django 4.2.5 on 2024-04-13 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_rename_exp_month_bank_exp_date_remove_bank_exp_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='mock_question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
            options={
                'db_table': 'mock_question',
            },
        ),
    ]
