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
from django.contrib.admin import ModelAdmin, register
from .models import Pagamento
from daterange_filter.filter import DateRangeFilter


@register(Pagamento)
class PagamentoAdmin(ModelAdmin):
    date_hierarchy = 'data_empenho'
    search_fields = ['vinculo__prestador__nome_apresentacao', 'vinculo__prestador__nome_civil',
                     'vinculo__prestador__nome_social', 'vinculo__prestador__cpf', 'vinculo__prestador__numero_siape', ]
    list_display = ['id', 'data_empenho', 'valor', 'nome', 'funcao', 'edital', ]
    list_filter = [('data_empenho', DateRangeFilter), 'vinculo__vaga__edital__identificacao',
                   'vinculo__vaga__funcao', 'vinculo__vaga__funcao__jornada', 'vinculo__eh_servidor', ]
    list_select_related = ('vinculo', 'vinculo__prestador',
                           'vinculo__vaga', 'vinculo__vaga__funcao', 'vinculo__vaga__edital')

    def nome(self, obj):
        return obj.vinculo.prestador.nome_apresentacao
    nome.admin_order_field = 'vinculo__prestador__nome_apresentacao'

    def funcao(self, obj):
        return obj.vinculo.vaga.funcao.nome
    funcao.admin_order_field = 'vinculo__vaga__funcao__nome'
    funcao.short_description = 'Função'

    def edital(self, obj):
        return obj.vinculo.vaga.edital.identificacao
    edital.admin_order_field = 'vinculo__vaga__edital__identificacao'
