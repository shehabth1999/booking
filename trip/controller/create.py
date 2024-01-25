from django.db import models


class Malti_Create_ALl_DBs(models.Manager):
    def create(self, **kwargs):
        instance = super().create(**kwargs)
        self.using('second').create(**kwargs)
        return instance
