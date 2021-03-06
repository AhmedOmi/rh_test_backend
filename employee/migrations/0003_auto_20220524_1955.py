# Generated by Django 3.2.13 on 2022-05-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hired_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.CharField(blank=True, choices=[('DevOps_team', 'DevOps_team'), ('Dev_team', 'Dev_team'), ('Design_team', 'Design_team')], max_length=15, null=True),
        ),
    ]
