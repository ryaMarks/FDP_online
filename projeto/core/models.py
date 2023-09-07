from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Classe com as datas de criação e modificacao
class TimeStampedModel(models.Model):

    # pega a data de criacao de um item
    created = models.DateTimeField(
        'criado em ',
        auto_now_add=True,
        auto_now=False
    )
    # pega a data de modificacao de um item
    modified = models.DateTimeField(
        'modificado em ',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:  # essa classe sera herdada para outros models
        abstract = True  # abstração herança de classe habilitada



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(null=True, blank=True)