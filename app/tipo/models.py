# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from django.db.models import Model, CharField
from python_brfied import to_choice

class TipoAbstract(Model):
    nome = CharField('Nome', max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class DocumentacaoPessoal(TipoAbstract):

    class Meta:
        verbose_name = 'Documentação pessoal'
        verbose_name_plural = 'Documentações pessoais'
        ordering = ['nome']


class DocumentacaoCurricular(TipoAbstract):

    class Meta:
        verbose_name = 'Documentação curricular'
        verbose_name_plural = 'Documentações curriculares'
        ordering = ['nome']


class Programa(TipoAbstract):

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'
        ordering = ['nome']


class Funcao(TipoAbstract):
    SEMANAL = 'Semanal'
    MENSAL = 'Mensal'
    CHOICES = to_choice(SEMANAL, MENSAL)
    jornada = CharField('Jornada', max_length=10, choices=CHOICES, default=SEMANAL)

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'
        ordering = ['nome']
