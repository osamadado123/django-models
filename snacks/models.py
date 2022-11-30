from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack (models.Model):

    name = models.CharField(max_length=64,help_text='name of snack',default='snack')
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description=models.TextField(default='No description')

    def __str__(self) -> str:
        return self.name