from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from auditlog.apps import AuditlogConfig
from django.utils.translation import ugettext_lazy as _


class AuditlogCustomConfig(AuditlogConfig):
    verbose_name = _('Auditing')


class CoreConfig(AppConfig):
    name = 'gringo_tv.core'
    verbose_name = 'Gringo TV'


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
