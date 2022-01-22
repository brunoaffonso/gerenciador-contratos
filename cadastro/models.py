from django.db import models

class Unidade(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    obs = models.TextField(blank=True, default="")

    def __str__(self):
        return self.nome


class Fiscal(models.Model):
    VINCULO = (
        ('Servidor', 'Servidor'),
        ('Terceirizado', 'Terceirizado')
    )
    DISCIPLINA = (
        ('Telecomunicações', 'Telecomunicações'),
        ('Arquitetura', 'Arquitetura'),
        ('Elétrica', 'Elétrica'),
        ('Estruturas', 'Estruturas')
    )

    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()
    cpf = models.IntegerField()
    vinculo = models.CharField(max_length=12, choices=VINCULO)
    disciplina = models.CharField(max_length=20, choices=DISCIPLINA)
    obs = models.TextField(blank=True, default="")

    def __str__(self):
        return self.nome

