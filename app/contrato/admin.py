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
from django.contrib.admin import register, ModelAdmin, StackedInline, TabularInline
from .models import Edital, Vaga, Prestador, Vinculo, DocumentacaoPessoal, DocumentacaoCurricular, Reserva, Contato


class VagaInline(TabularInline):
    model = Vaga
    classes = ['collapse']
    extra = 0


class DocumentacaoPessoalInline(TabularInline):
    model = DocumentacaoPessoal
    fields = ['tipo', 'valor', 'arquivo', 'observacao', ]
    classes = ['collapse']
    extra = 0


class DocumentacaoCurricularInline(TabularInline):
    model = DocumentacaoCurricular
    fields = ['tipo', 'valor', 'arquivo', 'observacao', ]
    classes = ['collapse']
    extra = 0


class ContatoInline(TabularInline):
    model = Contato
    classes = ['collapse']
    extra = 0


@register(Edital)
class EditalAdmin(ModelAdmin):
    inlines = [VagaInline]
    search_fields = ['identificacao', 'descricao', ]
    list_display = ['identificacao', 'descricao', 'programa', ]
    list_select_related = ('programa', )
    list_filter = ('programa__nome', )


@register(Prestador)
class PrestadorAdmin(ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('cpf', 'nome_civil', 'nome_social', 'nome_mae', 'nome_pai', 'data_nascimento', 'sexo',
                       'numero_siape')
        }),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': ('endereco_logradouro', 'endereco_numero', 'endereco_complemento', 'endereco_bairro',
                       'endereco_municipio', 'endereco_cep', 'endereco_referencia', 'endereco_zona', ),
        }),
        ('Dados bancários', {
            'classes': ('collapse',),
            'fields': ('banco', 'agencia', 'conta_corrente'),
        }),
        ('Observações', {
            'classes': ('collapse',),
            'fields': ('observacao',),
        }),
    )
    inlines = [DocumentacaoPessoalInline, ContatoInline, ]
    search_fields = ['nome_apresentacao', 'nome_civil', 'nome_social', 'cpf', 'numero_siape', 'observacao']
    list_display = ['nome_apresentacao', 'cpf', 'numero_siape', 'sexo', ]
    list_filter = ('sexo', )


@register(Vinculo)
class VinculorAdmin(ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('prestador', 'vaga', 'eh_servidor', 'valor_carga_horaria', )
        }),
        ('Empenho', {
            # 'classes': ('collapse',),
            'fields': ('data_empenho', 'numero_empenho', 'valor_total_empenho', ),
        }),
        ('Período', {
            # 'classes': ('collapse',),
            'fields': ('data_inicio_previsto', 'data_fim_previsto', 'data_inicio', 'data_fim_real', ),
        }),
        ('Observações', {
            'classes': ('collapse',),
            'fields': ('observacao',),
        }),
    )
    inlines = [DocumentacaoCurricularInline]
    search_fields = ['prestador__nome_apresentacao', 'prestador__nome_civil', 'prestador__nome_social',
                     'prestador__cpf', 'prestador__numero_siape', ]
    list_display = ['prestador', 'vaga']
    list_filter = ['eh_servidor', 'vaga__edital__identificacao', 'vaga', 'vaga__funcao',
                   'vaga__funcao__jornada', ]


@register(Reserva)
class ReservaAdmin(ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('prestador', 'ordem', 'vaga', )
        }),
        ('Período', {
            'classes': ('collapse',),
            'fields': ('convocado_em', 'assumiu_em', 'desistencia_em', 'termo_desistencia', ),
        }),
        ('Observações', {
            'classes': ('collapse',),
            'fields': ('observacao',),
        }),
    )
    search_fields = ['prestador__nome_apresentacao', 'prestador__nome_civil', 'prestador__nome_social',
                     'prestador__cpf', 'prestador__numero_siape', 'observacao', ]
    list_display = ['prestador', 'vaga', 'ordem', 'convocado_em', 'assumiu_em', 'desistencia_em',
                    'termo_desistencia', ]
    date_hierarchy = 'convocado_em'
    list_filter = ['ordem', 'vaga__edital__identificacao', 'vaga', 'vaga__funcao',
                   'vaga__funcao__jornada', 'convocado_em', 'assumiu_em', ]
