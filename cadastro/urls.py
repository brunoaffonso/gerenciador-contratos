from django.urls import path
from .views import UnidadeCreateView
from .views import UnidadeDetailView
from .views import UnidadeUpdateView
from .views import UnidadeDeleteView
from .views import UnidadeListView
from .views import FiscalCreateView
from .views import FiscalDetailView
from .views import FiscalUpdateView
from .views import FiscalDeleteView
from .views import FiscalListView
from.views import lista_cadastros


urlpatterns = [
    path('', lista_cadastros, name='lista-cadastros'),
    path('unidade/cria/', UnidadeCreateView.as_view(), name='cria-unidade'),
    path('unidade/ver/<pk>', UnidadeDetailView.as_view(), name='ver-unidade'),
    path('unidade/edita/<pk>', UnidadeUpdateView.as_view(), name='atualiza-unidade'),
    path('unidade/delete/<pk>', UnidadeDeleteView.as_view(), name='deleta-unidade'),
    path('unidade/lista/', UnidadeListView.as_view(), name='lista-unidade'),
    path('fiscal/cria/', FiscalCreateView.as_view(), name='cria-fiscal'),
    path('fiscal/ver/<pk>', FiscalDetailView.as_view(), name='ver-fiscal'),
    path('fiscal/edita/<pk>', FiscalUpdateView.as_view(), name='atualiza-fiscal'),
    path('fiscal/delete/<pk>', FiscalDeleteView.as_view(), name='deleta-fiscal'),
    path('fiscal/lista/', FiscalListView.as_view(), name='lista-fiscal'),
]