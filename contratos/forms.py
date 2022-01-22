from django.forms import ModelForm
from .models import Processo
from .models import Medicao


class ProcessoForm(ModelForm):
    class Meta:
        model = Processo
        fields = ['numero',
                  'nome',
                  'descricao',
                  'tipo',
                  'unidade',
                  'empresa',
                  'valor_inicial',
                  'valor_contratado',
                  'data_inicio',
                  'data_fim',
                  'fiscal',
                  'ativo',
                  'obs']


class MedicaoForm(ModelForm):
    class Meta:
        model = Medicao
        fields = ['data_1',
                  'data_2',
                  'valor_1',
                  'valor_2',
                  'obs']


class EventosForm(ModelForm):
    class Meta:
        model = Medicao
        fields = ['data_1',
                  'valor_1',
                  'obs']


class MedicaoContForm(ModelForm):
    class Meta:
        model = Medicao
        fields = ['data_1',
                  'data_2',
                  'valor_1',
                  'obs']


class ApostilamentoContForm(ModelForm):
    class Meta:
        model = Medicao
        fields = ['data_1',
                  'data_2',
                  'valor_1',
                  'obs']