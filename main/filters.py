import django_filters as filters

from django_filters import DateFilter

from .models import Conferencia, Produto

class ConferenciaFilter(filters.FilterSet):
    
    #data_conferencia = filters.CharFilter(label='Data da Conferência')
    
    class Meta:
        model = Conferencia
        fields = ('data_conferencia',)
        # exclude = ['funcionario']
    
    def __init__(self, *args, **kwargs):
        super(ConferenciaFilter, self).__init__(*args, **kwargs)
        self.filters['data_conferencia'].label = 'Data da Conferência'
    
class ProdutoFilter(filters.FilterSet):
    class Meta: 
        model = Produto
        fields = ('codigo_barras',)
