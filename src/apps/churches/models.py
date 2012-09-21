# -*- coding: utf8 -*-

from django.db import models


class Church(models.Model):
    """Modelo que representa o modelo de Igreja
    no sistema. Ele será usado para "encapsular" todas
    as informações da igreja como::

        - Ministérios;
        - Membros;
        - etc.

    Os campos dessa classe são::

        :param name: Nome da igreja
        :param address: Endereço da igreja
        :param site: Site da igreja
        :param email: E-mail da igreja
        :param phone: Telefone da igreja
        :param members: Quantidade total de membros
    """
    name = models.CharField(u"Nome da Igreja", max_length=100)
    address = models.CharField(u"Endereço", max_length=100)
    site = models.URLField(u"Site da Igreja")
    email = models.EmailField(u"E-mail")
    phone = models.CharField(u"Telefone", max_length=14)
    members = models.PositiveIntegerField(u"Total de Membros")

    class Meta:
        verbose_name = u"Igreja"
        verbose_name_plural = u"Igrejas"

    def __unicode__(self):
        return u'Church: %s' % (self.name,)
