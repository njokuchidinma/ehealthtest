# Generated by Django 4.1 on 2023-07-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_appointments_worker_alter_appointments_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]