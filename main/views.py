from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.urls import reverse

from django.core.exceptions import ValidationError

# from django.forms.models import inlineformset_factory

# DetailView -> Lista os detalhes
# ListView -> Lista os posts

# from django.views.generic import DetailView, ListView

from .models import Produto, Conferencia, Validade_Produto, Funcionario
from .filters import *
from .forms import ConferenciaForm, ValidadeProdutoForm

'''
class ProdutoListView(ListView):
    model = Produto
    
class ProdutoDetailView(DetailView):
    model = Produto

class ConferenciaListView(ListView):
    model = Conferencia

class ConferenciaDetailView(DetailView):
    model = Conferencia

class ValidadeProdutoListView(ListView):
    model = Validade_Produto

class ValidadeProdutoDetailView(DetailView):
    model = Validade_Produto
'''

'''
def produto_list(request):
    produtos = Produto.objects.all().order_by('codigo') # Pega todos os produtos
    return render(request, 'main/produto_list.html', {'produtos': produtos})

def produto_detalhes(request, slug):
    produto = get_object_or_404(Produto, slug=slug)
    return render(request, 'main/produto_detail.html', {'produto':produto})
'''
@login_required
def index(request):
    #form = Funcionario.objects.get(id=4)
    return render(request, 'main/index.html')

@login_required
def conferencia_list(request):
    conferencias = Conferencia.objects.all()
    filtro = ConferenciaFilter(request.GET, queryset = conferencias)
    conferencias = filtro.qs
    return render(request, 'main/conferencia_list.html', {'conferencias': conferencias, 'filtro': filtro})

'''
@login_required
def produto_list(requsest, codigo_barras):
    produtos = Produto.objects.all()
    filtro = ProdutoFilter(request.GET, queryset = produtos)
    produtos = filtro.qs

    return render(request, 'main/produto_list.html', {'Produtos': produtos, 'filtro': filtro})
'''

@login_required
def detalhes_conferencia(request, id):
    # conferencia = get_object_or_404(Validade_Produto, id=id)
    produtos_conferencia = Validade_Produto.objects.filter(conferencia_id = id).order_by('codigo_barras')
    print("detalhes_conferencia")
    return render(request, 'main/conferencia_detail.html', {'produtos_conferencia':produtos_conferencia})

@login_required
def nova_conferencia(request):
    print("nova_conferencia")         
    formulario_conferencia = ConferenciaForm()
    print(request.method)

    if request.method == 'POST':
        print("if")
        formulario_conferencia = ConferenciaForm(request.POST)

        if(formulario_conferencia.is_valid()):
            print("válido")
            nova_conferencia = formulario_conferencia.save(commit=False)
            func_id = request.user.id
            funcionario = Funcionario.objects.get(usuario_id = func_id)
            corredor_conferencia = formulario_conferencia.cleaned_data['corredor']
            
            nova_conferencia = Conferencia(corredor = corredor_conferencia, funcionario=funcionario)
            nova_conferencia.save()
            
            id_conferencia = nova_conferencia.id

            print('func: ',func_id)
            print('corredor: ',corredor_conferencia)  
            context = {'id_conf': id_conferencia}
            print(context)
            # print(reverse('detalhes_conferencia', id_conferencia))
            #else:
                #print(formulario_validade_produtos.errors)

            # return redirect(reverse('detalhes_conferencia', id_conferencia))
            # return redirect('/conferencias/'+str(id_conferencia)) # redirecionar para a página de adição de itens
            return redirect('/nova-conferencia-itens/') # redirecionar para a página de adição de itens

    elif(request.method == 'GET'):
        formulario_conferencia = ConferenciaForm()    
        
        # Se for um get, redireciona pra página de nova conferência
    return render(request, 'main/nova_conferencia.html', {'form': formulario_conferencia})

def nova_conferecia_itens(request):
    form = ValidadeProdutoForm()

    if request.method == 'POST':
        print('método post')
        formulario_validade_produtos = ConferenciaForm(request.POST) 
        
        if (formulario_validade_produtos.is_valid()):
            codigo_barras = formulario_validade_produtos.cleaned_data['data_barras']
            data_validade = formulario_validade_produtos.cleaned_data['data_validade']
            quantidade = formulario_validade_produtos.cleaned_data['validade']

            produto = Validade_Produto(
                codigo_barras=codigo_barras, 
                conferencia=id_conferencias, 
                data_validade=data_validade, 
                quantidade=quantidade)     

            return render(request, 'main/nova_conferencia_itens.html', {'form': formulario_validade_produtos})

    elif request.method == 'GET':
        form = ValidadeProdutoForm()
    
    return render(request, 'main/nova_conferencia_itens.html', {'form': form})


def busca_produto(request, codigo_barras):
    produto = Produto.objects.get(codigo_barras=codigo_barras)

    

'''
            print(formulario_validade_produtos['codigo_barras'].value())
            campo_codigo = formulario_validade_produtos['codigo_barras'].value()

            try:
                produto = Produto.objects.get(codigo_barras='7894561230')
            except Produto.DoesNotExist:
                raise ValidationError("Produto não encontrado")
'''

'''
            codigo = produto
            data_validade = formulario_validade_produtos.cleaned_data['data_validade']
            quantidade = formulario_validade_produtos.cleaned_data['quantidade'] 

            print(codigo)
            print(data_validade)
            print(quantidade)

            produto = Validade_Produto(codigo_barras=codigo, conferencia=nova_conferencia, data_validade=data_validade, quantidade=quantidade)
            produto.save()  
'''