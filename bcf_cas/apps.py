# bcf_cas/apps.py
# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BCFCASConfig(AppConfig):
    """
    For Django 1.9 compatibility
    """
    name = 'bcf_cas'
    label = 'bcf_cas'
    verbose_name = _("BCF CAS Core")
