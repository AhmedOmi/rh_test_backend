# Generated by Django 3.2.13 on 2022-05-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.CharField(choices=[('DevOps_team', 'DevOps_team'), ('Dev_team', 'Dev_team'), ('Design_team', 'Design_team')], max_length=15, null=True),
        ),
    ]
