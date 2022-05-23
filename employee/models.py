from django.db import models
from sqlalchemy import false


class Employee(models.Model):

    TEAMS = (
        ("DevOps_team", "DevOps_team"),
        ("Dev_team", "Dev_team"),
        ("Design_team", "Design_team")
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField()
    hired_on = models.DateTimeField()
    position = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    is_manager = models.BooleanField(default=False)
    team = models.CharField(max_length=15, choices=TEAMS, null=True)

    def __str__(self):
        return self.name
