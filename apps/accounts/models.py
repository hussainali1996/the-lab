# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Partner(models.Model):
    """
    This model represents white-labelled partners.
    """
    label = models.CharField(max_length=100)
    main_logo = models.CharField(max_length=255)
    small_logo = models.CharField(max_length=255)
    slug = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return '{}'.format(self.label)

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
