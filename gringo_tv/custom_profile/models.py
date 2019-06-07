from auditlog.registry import auditlog

from django.db import models
from django.contrib.auth import get_user_model

from gringo_tv.dealer.models import Dealer
from gringo_tv.custom_profile import manager
from gringo_tv.core.models import AbstractBaseModel


User = get_user_model()


class Profile(AbstractBaseModel):

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfils'

    user = models.OneToOneField(User, verbose_name='Usuário', on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(verbose_name='Telefone', max_length=11)
    points = models.IntegerField(verbose_name='Pontos', default=0)

    def __str__(self):
        return self.user.get_full_name()


class Indication(AbstractBaseModel):

    class Meta:
        verbose_name = 'Indicação'
        verbose_name_plural = 'Indicações'
        ordering = ['-status']

    PENDING = 'pending'
    NOT_ACTIVE = 'not_active'
    ACTIVE = 'active'

    STATUS = [
        (PENDING, 'Pendente'),
        (NOT_ACTIVE, 'Não Ativo'),
        (ACTIVE, 'Ativo')
    ]

    objects = manager.IndicationManager()

    profile = models.ForeignKey(Profile, verbose_name='Perfil', on_delete=models.CASCADE, related_name='indications')
    dealer = models.ForeignKey(Dealer, verbose_name='Revendedor', on_delete=models.CASCADE, related_name='profiles')
    status = models.CharField(verbose_name='Status', max_length=255, choices=STATUS, default=PENDING)
    name = models.CharField(verbose_name='Nome', max_length=255)
    phone = models.CharField(verbose_name='Telefone', max_length=11)

    def save(self):
        if self.status == self.ACTIVE:
            self.profile.points += 1
            self.profile.save()
        return super().save()

    @property
    def is_active(self):
        return self.status == self.ACTIVE

    @property
    def is_pending(self):
        return self.status == self.PENDING

    @property
    def is_not_active(self):
        return self.status == self.NOT_ACTIVE


auditlog.register(User)
auditlog.register(Profile)
auditlog.register(Indication)
