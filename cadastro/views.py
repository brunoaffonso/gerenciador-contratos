from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Unidade, Fiscal


class UnidadeListView(ListView):
    model = Unidade


class FiscalListView(ListView):
    model = Fiscal


class UnidadeCreateView(CreateView):
    model = Unidade
    fields = ['nome', 'descricao', 'cidade', 'estado', 'obs']
    success_url = reverse_lazy('lista-cadastros')


class FiscalCreateView(CreateView):
    model = Fiscal
    fields = ['nome',
              'matricula',
              'cpf',
              'vinculo',
              'disciplina',
              'obs']
    success_url = reverse_lazy('lista-cadastros')


class UnidadeDetailView(DetailView):
    model = Unidade


class FiscalDetailView(DetailView):
    model = Fiscal


class UnidadeUpdateView(UpdateView):
    model = Unidade
    fields = ['nome', 'descricao', 'cidade', 'estado', 'obs']
    success_url = reverse_lazy('lista-cadastros')


class FiscalUpdateView(UpdateView):
    model = Fiscal
    fields = ['nome',
              'matricula',
              'cpf',
              'vinculo',
              'disciplina',
              'obs']
    success_url = reverse_lazy('lista-cadastros')


class UnidadeDeleteView(DeleteView):
    model = Unidade
    success_url = reverse_lazy('lista-cadastros')


class FiscalDeleteView(DeleteView):
    model = Fiscal
    success_url = reverse_lazy('lista-cadastros')


def lista_cadastros(request):
    unidade = Unidade.objects.all()
    fiscal = Fiscal.objects.all()
    return render(request, 'lista_cadastro.html', {'u': unidade, 'f': fiscal})

