# -*- coding: utf8 -*-

from django.test import TestCase

from src.apps.churches.models import Church


class ChurchModelTest(TestCase):
    def setUp(self):
        self.church = Church.objects.create(
            name="Church Test",
            address="CLH 019",
            site="http://churchtest.org.br",
            email="mail@church.org.br",
            phone="(61) 1020-1928",
            members=100
        )

    def test_create(self):
        """Registra a igreja com sucesso"""
        self.assertEquals(self.church.pk, 1)

    def test_unicode(self):
        """Retorna a representação do objeto"""
        self.assertEquals('Church: %s', unicode(self.church))
