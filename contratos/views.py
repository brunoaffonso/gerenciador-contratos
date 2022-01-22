from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Processo
from .models import Medicao
from .forms import MedicaoForm
from .forms import EventosForm
from .forms import MedicaoContForm
from .forms import ApostilamentoContForm


class ProcessoListView(ListView):
    model = Processo


class MedicaoListView(ListView):
    model = Medicao


class ProcessoCreateView(CreateView):
    model = Processo
    fields = ['numero',
              'nome',
              'descricao',
              'tipo',
              'unidade',
              'empresa',
              'valor_inicial',
              'valor_contratado',
              'valor_atual',
              'data_inicio',
              'data_fim',
              'fiscal',
              'ativo',
              'obs']
    success_url = reverse_lazy('lista-processo')


class MedicaoCreateView(CreateView):
    model = Medicao
    fields = ['nome',
              'contrato',
              'evento',
              'data_1',
              'data_2',
              'valor_1',
              'valor_2',
              'obs']
    success_url = reverse_lazy('lista-processo')


class ProcessoDetailView(DetailView):
    model = Processo


class MedicaoDetailView(DetailView):
    model = Medicao


class ProcessoUpdateView(UpdateView):
    model = Processo
    fields = ['numero',
              'nome',
              'descricao',
              'tipo',
              'unidade',
              'empresa',
              'valor_inicial',
              'valor_contratado',
              'valor_atual',
              'data_inicio',
              'data_fim',
              'fiscal',
              'ativo',
              'obs']
    success_url = reverse_lazy('lista-processo')


class MedicaoUpdateView(UpdateView):
    model = Medicao
    fields = ['data_1',
              'data_2',
              'valor_1',
              'valor_2',
              'obs']
    success_url = reverse_lazy('lista-processo')


class ProcessoDeleteView(DeleteView):
    model = Processo
    success_url = reverse_lazy('lista-processo')


class MedicaoDeleteView(DeleteView):
    model = Medicao
    success_url = reverse_lazy('lista-medicao')


def processos(request):
    processos = Processo.objects.all()
    return render(request, 'lista_processos.html', {'processos' : processos})

def detalha_processo_tipo(request, id):
    processo = get_object_or_404(Processo, pk=id)
    medicao = Medicao.objects.all().filter(contrato_id=id).order_by('data_1')
    if processo.tipo == 'Obra':
        return render(request, 'detalhe_processo_obra.html', {'p': processo, 'm': medicao})
    else:
        return render(request, 'detalhe_processo_continuado.html', {'p': processo, 'm': medicao})


def adiciona_evento_obra(request, id, evento):
    contrato = get_object_or_404(Processo, id=id)
    nova_entrada = None
    evento_atual = evento

    if evento_atual == 'Apostilamento':
        evento_atual = 'Reajustamento'
        title = 'Cadastrar novo {}'.format(evento_atual)
    elif evento_atual == 'Aditivo de Acréscimo':
        evento_atual = 'Termo Aditivo de Acréscimo'
        title = 'Cadastrar novo {}'.format(evento_atual)
    elif evento_atual == 'Aditivo de Supressão':
        evento_atual = 'Termo Aditivo de Supressão'
        title = 'Cadastrar novo {}'.format(evento_atual)
    elif evento_atual == 'Medição':
        title = 'Cadastrar nova {}'.format(evento_atual)

    entradas_ant = Medicao.objects.all().filter(contrato_id=id, evento=evento).count()

    if request.method == 'POST':
        def save_form(form):
            nova_entrada = form.save(commit=False)
            nova_entrada.nome = "{}º {}".format(entradas_ant + 1, evento_atual)
            nova_entrada.evento = evento
            nova_entrada.contrato = contrato
            nova_entrada.save()

        if evento == 'Medição':
            form = MedicaoForm(request.POST)
            if form.is_valid():
                save_form(form)
                return redirect('ver-processo', id)
        else:
            form = EventosForm(request.POST)
            if form.is_valid():
                save_form(form)
                return redirect('ver-processo', id)
    else:
        if evento == 'Medição':
            form = MedicaoForm()
            return render(request, 'cria_medicao_obra.html', {'form': form, 'title': title})
        else:
            form = EventosForm()
            return render(request, 'evento.html', {'form': form, 'title': title})


def adiciona_evento_continuado(request, id, evento):
    contrato = get_object_or_404(Processo, id=id)
    nova_entrada = None
    evento_atual = evento

    if evento_atual == 'Apostilamento':
        evento_atual = 'Repactuação'
        title = 'Cadastrar nova {}'.format(evento_atual)
    elif evento_atual == 'Aditivo de Acréscimo':
        evento_atual = 'Termo Aditivo de Acréscimo'
        title = 'Cadastrar novo {}'.format(evento_atual)
    elif evento_atual == 'Aditivo de Supressão':
        evento_atual = 'Termo Aditivo de Supressão'
        title = 'Cadastrar novo {}'.format(evento_atual)
    elif evento_atual == 'Medição':
        title = 'Cadastrar nova {}'.format(evento_atual)

    entradas_ant = Medicao.objects.all().filter(contrato_id=id, evento=evento).count()

    if request.method == 'POST':
        def save_form(form):
            nova_entrada = form.save(commit=False)
            nova_entrada.nome = "{}º {}".format(entradas_ant + 1, evento_atual)
            nova_entrada.evento = evento
            nova_entrada.contrato = contrato
            nova_entrada.save()

        if evento == 'Medição':
            form = MedicaoContForm(request.POST)
            if form.is_valid():
                save_form(form)
                return redirect('ver-processo', id)
        elif evento == 'Apostilamento':
            form = ApostilamentoContForm(request.POST)
            if form.is_valid():
                save_form(form)
                return redirect('ver-processo', id)
        else:
            form = EventosForm(request.POST)
            if form.is_valid():
                save_form(form)
                return redirect('ver-processo', id)
    else:
        if evento == 'Apostilamento':
            form = ApostilamentoContForm()
            return render(request, 'cria_apostilamento_continuado.html', {'form': form, 'title': title})
        elif evento == 'Medição':
            form = MedicaoContForm()
            return render(request, 'cria_medicao_continuado.html', {'form': form, 'title': title})
        else:
            form = EventosForm()
            return render(request, 'cria_aditivo_continuado.html', {'form': form, 'title': title})


def edita_evento_obra(request, id_contrato, id_evento):
    dados = get_object_or_404(Medicao, id=id_evento)
    title = 'Editar {}'.format(dados.evento)

    if dados.evento == 'Medição':
        form = MedicaoForm(request.POST or None, instance=dados)
        if form.is_valid():
            form.save()
            return redirect('ver-processo', id_contrato)

        return render(request, 'cria_medicao_obra.html', {'form': form, 'title': title})

    else:
        form = EventosForm(request.POST or None, instance=dados)
        if form.is_valid():
            form.save()
            return redirect('ver-processo', id_contrato)

        return render(request, 'evento.html', {'form': form, 'title': title})


def edita_evento_continuado(request, id_contrato, id_evento):
    dados = get_object_or_404(Medicao, id=id_evento)
    title = 'Editar {}'.format(dados.evento)

    if dados.evento == 'Medição':
        form = MedicaoContForm(request.POST or None, instance=dados)
        if form.is_valid():
            form.save()
            return redirect('ver-processo', id_contrato)

        return render(request, 'cria_medicao_continuado.html', {'form': form, 'title': title})

    elif dados.evento == 'Apostilamento':
        form = ApostilamentoContForm(request.POST or None, instance=dados)
        if form.is_valid():
            form.save()
            return redirect('ver-processo', id_contrato)

        return render(request, 'cria_apostilamento_continuado.html', {'form': form, 'title': title})

    else:
        form = EventosForm(request.POST or None, instance=dados)
        if form.is_valid():
            form.save()
            return redirect('ver-processo', id_contrato)

        return render(request, 'evento.html', {'form': form, 'title': title})
