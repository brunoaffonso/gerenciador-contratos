from django.urls import path
from .views import ProcessoCreateView
from .views import ProcessoDetailView
from .views import ProcessoUpdateView
from .views import ProcessoDeleteView
from .views import ProcessoListView
from .views import MedicaoCreateView
from .views import MedicaoDetailView
from .views import MedicaoUpdateView
from .views import MedicaoDeleteView
from .views import MedicaoListView
from .views import processos
from .views import detalha_processo_tipo
from .views import adiciona_evento_obra
from .views import adiciona_evento_continuado
from .views import edita_evento_obra
from .views import edita_evento_continuado


urlpatterns = [
    path('processo/cria/', ProcessoCreateView.as_view(), name='cria-processo'),
    path('processo/ver/<id>', detalha_processo_tipo, name='ver-processo'),
    path('processo/ver2/<pk>', ProcessoDetailView.as_view(), name='ver-processo2'),
    path('processo/edita/<pk>', ProcessoUpdateView.as_view(), name='atualiza-processo'),
    path('processo/delete/<pk>', ProcessoDeleteView.as_view(), name='deleta-processo'),
    path('processo/lista/', processos, name='lista-processo'),
    path('processo/lista2/', ProcessoListView.as_view(), name='lista-processo2'),
    path('medicao/cria/', MedicaoCreateView.as_view(), name='cria-medicao'),
    path('medicao/ver/<pk>', MedicaoDetailView.as_view(), name='ver-medicao'),
    path('medicao/edita/<pk>', MedicaoUpdateView.as_view(), name='atualiza-medicao'),
    path('medicao/edita/obra/<id_contrato>/<id_evento>', edita_evento_obra, name='atualiza-evento-obra'),
    path('medicao/edita/continuado/<id_contrato>/<id_evento>', edita_evento_continuado, name='atualiza-evento-continuado'),
    path('medicao/delete/<pk>', MedicaoDeleteView.as_view(), name='deleta-medicao'),
    path('medicao/lista/', MedicaoListView.as_view(), name='lista-medicao'),
    path('medicao/adiciona/evento/obra/<id>/<evento>', adiciona_evento_obra, name='adiciona_evento_obra'),
    path('medicao/adiciona/evento/continuado/<id>/<evento>', adiciona_evento_continuado, name='adiciona_evento_continuado'),
]
