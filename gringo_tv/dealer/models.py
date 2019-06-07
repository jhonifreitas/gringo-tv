from auditlog.registry import auditlog

from django.db import models
from django.contrib.auth import get_user_model

from gringo_tv.core.models import AbstractBaseModel


User = get_user_model()


class Dealer(AbstractBaseModel):

    class Meta:
        verbose_name = 'Revendedor'
        verbose_name_plural = 'Revendedores'

    user = models.OneToOneField(User, verbose_name='Usuário', on_delete=models.CASCADE, related_name='dealer')
    phone = models.CharField(verbose_name='Telefone', max_length=11)


auditlog.register(Dealer)
