from django.forms import ModelForm
from .models import Unidade
from .models import Fiscal


class UnidadeForm(ModelForm):
    class Meta:
        model = Unidade
        fields = ['nome',
                  'descricao',
                  'cidade',
                  'estado',
                  'obs']


class FiscalForm(ModelForm):
    class Meta:
        model = Fiscal
        fields = ['nome',
                  'matricula',
                  'cpf',
                  'vinculo',
                  'disciplina',
                  'obs']
