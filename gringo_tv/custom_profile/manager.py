from gringo_tv.core.manager import Manager
from gringo_tv.custom_profile import models


class IndicationManager(Manager):

    def pending(self):
        return self.filter(status=models.Indication.PENDING).count()
