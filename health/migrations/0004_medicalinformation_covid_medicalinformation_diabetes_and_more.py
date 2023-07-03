# Generated by Django 4.1 on 2023-07-03 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_medicalinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalinformation',
            name='covid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalinformation',
            name='diabetes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalinformation',
            name='ebola',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalinformation',
            name='malaria',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]