from django.db import models

class just_user(models.Model):
    username = models.CharField(max_length=20, min_length=3)

