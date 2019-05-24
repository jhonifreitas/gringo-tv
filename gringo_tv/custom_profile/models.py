from auditlog.registry import auditlog

from django.db import models

from django.contrib.auth import get_user_model
from gringo_tv.core.models import AbstractBaseModel


User = get_user_model()


class Profile(AbstractBaseModel):

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfils'

    user = models.OneToOneField(User, verbose_name='Usuário', on_delete=models.CASCADE, related_name='profile')


auditlog.register(User)
auditlog.register(Profile)
