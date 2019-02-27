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
from django.db.models import Model, CharField, TextField, DateField, URLField, PositiveSmallIntegerField, \
                             DecimalField, BooleanField, FileField
# from django.contrib.postgres.fields import JSONField
from django_brfied.django_brfied.models import SexoField, ForeignKey
from django_brfied.django_brfied.mixin import EnderecoMixin
from python_brfied import to_choice
from tipo.models import Programa, Funcao, DocumentacaoPessoal as TipoDocumentacaoPessoal, \
                        DocumentacaoCurricular as TipoDocumentacaoCurricular


class Edital(Model):
    identificacao = CharField('Identificação do edital', max_length=250,
                              validators=[RegexValidator(regex='^\d*/\d{4} .+')],
                              help_text='Formato: 0001/2018 UORG-UORG-UORG - Evite colocar a descrição aqui')
    descricao = CharField('Descrição', max_length=250)
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
    carga_horaria = PositiveSmallIntegerField('Carga horária', validators=[MaxValueValidator(168)])

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return "%s (%s)" % (self.funcao, self.edital,)


class Prestador(EnderecoMixin):
    cpf = CharField('CPF', max_length=11)
    nome_civil = CharField('Nome civil', max_length=255, required=False)
    nome_social = CharField('Nome social', max_length=255, null=True, blank=True, required=False)
    nome_apresentacao = CharField('Nome', max_length=255, required=False)
    nome_mae = CharField('Nome da mãe', max_length=255, required=False)
    nome_pai = CharField('Nome do pai', max_length=255, null=True, blank=True, required=False)
    data_nascimento = DateField('Data de nascimento', required=False)
    sexo = SexoField(required=False)
    numero_siape = CharField('Número do SIAPE', max_length=7, null=True, blank=True)
    banco = CharField('Banco', max_length=250, null=True, blank=True, required=False)
    agencia = CharField('Agência', max_length=250, null=True, blank=True, required=False)
    conta_corrente = CharField('Conta', max_length=250, null=True, blank=True, required=False)
    observacao = TextField('Observações', null=True, blank=True, required=False)

    class Meta:
        verbose_name = 'Prestador'
        verbose_name_plural = 'Prestadores'

    def __str__(self):
        return "%s (%s)" % (self.nome_apresentacao, self.cpf)

    def save(self, *args, **kwargs):
        self.nome_apresentacao = self.nome_social if self.nome_social else self.nome_civil
        super().save(*args, **kwargs)


class Contato(Model):
    TIPO_TELEFONE = 'Telefone'
    TIPO_CELULAR = 'Celular'
    TIPO_VOIP = 'VoIP'
    TIPO_EMAIL = 'E-Mail'
    TIPO_IM = 'Instant Message'
    TIPO_SITE = 'Site'
    TIPO_ENDERECO = 'Endereço'
    TIPO_CHOICES = to_choice(TIPO_TELEFONE, TIPO_CELULAR, TIPO_VOIP, TIPO_EMAIL, TIPO_IM, TIPO_SITE, TIPO_ENDERECO)

    prestador = ForeignKey('Prestador', Prestador)
    tipo = CharField('Tipo', max_length=20, choices=TIPO_CHOICES)
    principal = BooleanField('Principal')
    nome = CharField('Nome', max_length=250, null=True, blank=True, required=False)
    valor = CharField('Contato', max_length=250, null=True, blank=True, required=False)
    observacao = TextField('Observações', null=True, blank=True, required=False)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return "%s (%s) - %s %s" % (self.nome, self.valor, self.tipo, self.principal, )


class Vinculo(Model):
    prestador = ForeignKey('Prestador', Prestador)
    vaga = ForeignKey('Vaga', Vaga)
    eh_servidor = BooleanField('É servidor?')
    data_empenho = DateField('Data do empenho', null=True, blank=True,required=False)
    numero_empenho = CharField('Número do empenho', max_length=20, null=True, blank=True,required=False)
    valor_total_empenho = DecimalField('Valor total do empenho', max_digits=10, decimal_places=2, null=True, blank=True,required=False)
    valor_carga_horaria = DecimalField('Valor por hora', max_digits=10, decimal_places=2,required=False)
    data_inicio_previsto = DateField('Data de início previsto',required=False)
    data_fim_previsto = DateField('Data de fim previsto',required=False)
    data_inicio = DateField('Data de início real', null=True, blank=True,required=False)
    data_fim_real = DateField('Data de fim real', null=True, blank=True,required=False)
    observacao = TextField('Observações', null=True, blank=True,required=False)

    class Meta:
        verbose_name = 'Vínculo'
        verbose_name_plural = 'Vínculos'

    def __str__(self):
        return "%s - %s" % (self.prestador, self.vaga)


class Reserva(Model):
    prestador = ForeignKey('Prestador', Prestador)
    vaga = ForeignKey('Vaga', Vaga)
    ordem = PositiveSmallIntegerField('Ordem')
    convocado_em = DateField('Convocado em', null=True, blank=True)
    assumiu_em = DateField('Assumiu em', null=True, blank=True)
    desistencia_em = DateField('Desistência em', null=True, blank=True)
    termo_desistencia = CharField('Termo desistência', max_length=250, null=True, blank=True)
    observacao = TextField('Observações', null=True, blank=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return "%s - %sº como %s" % (self.prestador, self.ordem, self.vaga)

    @property
    def status(self):
        if self.desistencia_em is not None:
            return 'desistiu'
        if self.assumiu_em is not None:
            return 'assumiu'
        if self.convocado_em is not None:
            return 'convocado'
        return 'reserva'


class DocumentacaoMixin(Model):
    valor = CharField('Identificação do documento', max_length=250,required=False)
    arquivo = FileField('Comprovante', max_length=250,required=False)
    data_envio = DateField('Envio', auto_now=True,required=False)
    observacao = TextField('Observações', null=True, blank=True,required=False)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s - %s" % (self.tipo, self.valor)


class DocumentacaoPessoal(DocumentacaoMixin):
    prestador = ForeignKey('Prestador', Prestador)
    tipo = ForeignKey('Tipo', TipoDocumentacaoPessoal)

    class Meta:
        verbose_name = 'Documentação pessoal'
        verbose_name_plural = 'Documentações pessoais'

    def __str__(self):
        return "%s - %s" % (self.tipo, self.valor)


class DocumentacaoCurricular(DocumentacaoMixin):
    vinculo = ForeignKey('Vinculo', Vinculo)
    tipo = ForeignKey('Tipo', TipoDocumentacaoCurricular)

    class Meta:
        verbose_name = 'Documentação curricular'
        verbose_name_plural = 'Documentações curriculares'
