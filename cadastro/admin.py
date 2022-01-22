from django.contrib import admin
from .models import Unidade
from .models import Fiscal


class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'descricao',
                    'cidade',
                    'estado')


class FiscalAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'matricula',
                    'cpf',
                    'vinculo')


admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Fiscal, FiscalAdmin)
