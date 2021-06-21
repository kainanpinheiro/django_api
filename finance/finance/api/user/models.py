from django import db
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_user')
    name = models.CharField(max_length=50, db_column='name')

    class Meta:
        db_table = 'user'
