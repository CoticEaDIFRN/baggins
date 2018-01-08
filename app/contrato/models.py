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
from django.core.validators import MaxValueValidator, RegexValidator
from django.db.models import Model, CharField, TextField, DateField, URLField, PositiveSmallIntegerField, FloatField, \
                             BooleanField
from django_brfied.django_brfied.models import SexoField, ForeignKey
from django_brfied.django_brfied.mixin import EnderecoMixin
from tipo.models import Programa, Funcao


class Edital(Model):
    identificacao = CharField('Identificação', max_length=250, validators=[RegexValidator(regex='^\d*/\d{4} .+')])
    link = URLField()
    programa = ForeignKey('Programa', Programa)

    class Meta:
        verbose_name = 'Edital'
        verbose_name_plural = 'Editais'

    def __str__(self):
        return self.identificacao


class Vaga(Model):
    edital = ForeignKey('Edital', Edital)
    funcao = ForeignKey('Função', Funcao)
    carga_horaria = PositiveSmallIntegerField('Função', validators=[MaxValueValidator(40)])

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return "%s do edital %s" % (self.funcao, self.edital,)


class Prestador(EnderecoMixin):
    cpf = CharField('CPF', max_length=11)
    nome_civil = CharField('Nome civil', max_length=255)
    nome_social = CharField('Nome social', max_length=255, null=True, blank=True)
    nome_apresentacao = CharField('Nome', max_length=255)
    nome_mae = CharField('Nome da mãe', max_length=255)
    nome_pai = CharField('Nome do pai', max_length=255, null=True, blank=True)
    data_nascimento = DateField('Data de nascimento')
    sexo = SexoField()
    numero_siape = CharField('Número do SIAPE', max_length=7, null=True, blank=True)
    banco = CharField('Banco', max_length=250, null=True, blank=True)
    agencia = CharField('Agência', max_length=250, null=True, blank=True)
    conta_corrente = CharField('Conta', max_length=250, null=True, blank=True)
    observacao = TextField('Observações', null=True, blank=True)

    class Meta:
        verbose_name = 'Prestador'
        verbose_name_plural = 'Prestadores'

    def __str__(self):
        return "%s (%s)" % (self.nome_apresentacao, self.cpf)

    def save(self, *args, **kwargs):
        self.nome_apresentacao = self.nome_social if self.nome_social else self.nome_civil
        super().save(*args, **kwargs)


class Vinculo(Model):
    prestador = ForeignKey('Prestador', Prestador)
    vaga = ForeignKey('Vaga', Vaga)
    eh_servidor = BooleanField('É servidor?')
    data_empenho = DateField('Data do empenho', null=True, blank=True)
    numero_empenho = CharField('Número do empenho', max_length=20, null=True, blank=True)
    valor_total_empenho = FloatField('Valor total do empenho', null=True, blank=True)
    valor_carga_horaria = FloatField('Valor por hora')
    data_inicio_previsto = DateField('Data de início previsto')
    data_fim_previsto = DateField('Data de fim previsto')
    data_inicio = DateField('Data de início real', null=True, blank=True)
    data_fim_real = DateField('Data de fim real', null=True, blank=True)
    observacao = TextField('Observações', null=True, blank=True)

    class Meta:
        verbose_name = 'Vínculo'
        verbose_name_plural = 'Vínculos'

    def __str__(self):
        return "%s - %s" % (self.prestador, self.vaga)
