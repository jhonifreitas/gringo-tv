from uuid import uuid4
from cloudinary.models import CloudinaryField
from auditlog.models import AuditlogHistoryField

from django.db import models
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
        result = str(self.pk)
        if hasattr(self, 'title'):
            result = self.title
        elif hasattr(self, 'name'):
            result = self.name
        return result


def get_config_path(instance, filename):
    return get_storage_path(filename, 'config')


class Config(AbstractBaseModel):

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configuração'

    image = CloudinaryField(verbose_name='Imagem', null=True, blank=True)
    # image = models.ImageField(verbose_name='Imagem', upload_to=get_config_path, null=True, blank=True)
    datetime = models.DateTimeField(verbose_name='Data/Hora')
    description = models.TextField(verbose_name='Descrição')
