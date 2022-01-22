from django.contrib import admin
from .models import Processo
from .models import Medicao


class ProcessoAdmin(admin.ModelAdmin):
    list_display = ('numero',
                    'nome',
                    'descricao',
                    'tipo',
                    'unidade',
                    'empresa',
                    'valor_contratado',
                    'data_inicio',
                    'data_fim',
                    'ativo')


class MedicaoAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'contrato',
                    'data_1',
                    'data_2',
                    'valor_1',
                    'valor_2')


admin.site.register(Processo, ProcessoAdmin)
admin.site.register(Medicao, MedicaoAdmin)