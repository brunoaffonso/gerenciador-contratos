from django.db import models
from cadastro.models import Unidade
from cadastro.models import Fiscal
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver


class Processo(models.Model):
    TIPO_CONTRATO = (
        ('Obra', 'Obra'),
        ('Continuado', 'Continuado'),
    )

    numero = models.IntegerField()
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=250)
    tipo = models.CharField(max_length=10, choices=TIPO_CONTRATO)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    empresa = models.CharField(max_length=100)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    valor_contratado = models.DecimalField(max_digits=10, decimal_places=2)
    valor_atual = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    fiscal = models.ManyToManyField(Fiscal)
    ativo = models.BooleanField(default=False)
    percent_acres = models.FloatField(default=0)
    percent_sup = models.FloatField(default=0)
    percent_med = models.FloatField(default=0)
    percent_apost = models.FloatField(default=0)
    processo_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None)
    obs = models.TextField(blank=True, default="")

    def calcula_evento(self):
        medicao = Medicao.objects.filter(contrato=self).last()
        if medicao.contrato.tipo == 'Obra':
            if medicao.evento == 'Medição':
                percent = medicao.percent_event
                if self.valor_atual != '':
                    self.percent_med += percent
                    self.valor_atual += medicao.valor_2
                    self.save()
                else:
                    self.percent_med += percent
                    self.valor_atual += medicao.valor_2
                    self.save()
            elif medicao.evento == 'Apostilamento':
                percent = medicao.percent_event
                self.percent_apost += percent
                self.valor_contratado += medicao.valor_1
                self.save()
            elif medicao.evento == 'Aditivo de Acréscimo':
                percent = medicao.percent_event
                self.percent_acres += percent
                self.valor_contratado += medicao.valor_1
                self.save()
            elif medicao.evento == 'Aditivo de Supressão':
                percent = medicao.percent_event
                self.percent_sup += percent
                self.valor_contratado -= medicao.valor_1
                self.save()

        else:
            if medicao.evento == 'Medição':
                percent = medicao.percent_event
                self.percent_med += percent
                self.valor_atual += medicao.valor_1
                self.save()
            elif medicao.evento == 'Apostilamento':
                percent = medicao.percent_event
                self.percent_apost += percent
                self.valor_contratado += medicao.valor_1
                self.save()
            elif medicao.evento == 'Aditivo de Acréscimo':
                percent = medicao.percent_event
                self.percent_acres += percent
                self.valor_contratado += medicao.valor_1
                self.save()
            elif medicao.evento == 'Aditivo de Supressão':
                percent = medicao.percent_event
                self.percent_sup += percent
                self.valor_contratado -= medicao.valor_1
                self.save()

    def subtrai_valores(self):
        medicao = Medicao.objects.filter(contrato=self).last()
        percent = medicao.percent_event
        self.percent_med -= percent
        self.valor_atual -= medicao.valor_1
        self.save()

    def edita_evento(self):
        pass

    def __str__(self):
        return str(self.numero) + ' - ' + str(self.unidade) + ' - ' + str(self.nome)


class Medicao(models.Model):
    EVENTO = (
        ('Medição', 'Medição'),
        ('Apostilamento', 'Apostilamento'),
        ('Aditivo de Acréscimo', 'Aditivo de Acréscimo'),
        ('Aditivo de Supressão', 'Aditivo de Supressão'),
    )

    nome = models.CharField(max_length=30)
    contrato = models.ForeignKey(Processo, on_delete=models.CASCADE)
    evento = models.CharField(max_length=30, choices=EVENTO)
    data_1 = models.DateField()
    data_2 = models.DateField(null=True)
    valor_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    origem = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None)
    percent_event = models.FloatField(default=0)
    obs = models.TextField(blank=True, default="")

    def __str__(self):
        return str(self.contrato) + ' - ' + str(self.nome)


@receiver(pre_save, sender=Medicao)
def salva_porcentagem_medicao(sender, instance, **kwargs):
    # if instance.evento:
    #     instance.contrato.edita_evento()
    # #TODO Verificar se evento existe e não salvar novamente, pois se existe, é edição.
    # #TODO Verificar no Pré Save se a instancia está criada, caso positivo, não somar valores. Checar o id da instancia a ser medida e subtrair o valor antigo e prosseguir para o save guardar o novo valor.

    if instance.id:
        pass

    total = instance.contrato.valor_contratado
    if instance.contrato.tipo == 'Obra' and instance.evento == 'Medição':
        valor = instance.valor_2
    else:
        valor = instance.valor_1
    percent = float((valor * 100) / total)
    instance.percent_event = percent


@receiver(post_save, sender=Medicao)
def salva_evento(sender, instance, **kwargs):
    instance.contrato.calcula_evento()


@receiver(pre_delete, sender=Medicao)
def exclui_evento(sender, instance, **kwargs):
    instance.contrato.subtrai_valores()
