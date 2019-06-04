import json
from uuid import uuid4

from auditlog.models import AuditlogHistoryField

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from gringo_tv.core.manager import Manager
from gringo_tv.storage import get_storage_path
from gringo_tv.core.signals import post_soft_delete


class AbstractBaseModel(models.Model):

    class Meta:
        abstract = True

    history = AuditlogHistoryField()
    uuid = models.UUIDField(verbose_name='UUID', default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), auto_now=True)
    deleted_at = models.DateTimeField(verbose_name=_('Deleted at'), null=True, blank=True)
    objects = Manager()
    objects_all = models.Manager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        post_soft_delete.send(sender=type(self), instance=self, using=self._state.db)

    def __str__(self):
        return str(self.pk)


def get_config_path(instance, filename):
    return get_storage_path(filename, 'config')


class Config(AbstractBaseModel):

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configuração'

    image = models.ImageField(verbose_name='Imagem', upload_to=get_config_path)
    datetime = models.DateTimeField(verbose_name='Data/Hora')
    description = models.TextField(verbose_name='Descrição')

    def get_image(self):
        return json.dumps({
            'name': self.image.name.split('/')[-1],
            'size': self.image.size,
            'url': settings.MEDIA_URL+self.image.name
        })
