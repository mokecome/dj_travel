from django.db import models
class User(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    passwd = models.CharField(max_length=12)
    class Meta:
        db_table = "user"
# Create your models here.
