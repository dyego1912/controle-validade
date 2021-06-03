from django.contrib import admin
from .models import (
    Categoria,
    Conferencia,
    ConferenciaItens,
    Corredor,
    Filial,
    Funcionario,
    Produto,
    Validade_Produto,
)


@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    fields = ('cargo', 'usuario', 'filial', )
    list_display = ('id', 'usuario', 'cargo', 'slug_filial', 'first_name')

    def slug_filial(self, obj):
        return obj.filial.slug

    def first_name(self, obj):
        return obj.usuario.first_name


@admin.register(Filial)
class Filial(admin.ModelAdmin):
    fields = ('nome', 'slug')
    list_display = ('nome',)


@admin.register(Corredor)
class Corredor(admin.ModelAdmin):
    fields = ('nome', 'descricao', 'filial', 'slug',)
    list_display = ('id', 'nome', 'descricao', 'slug', 'slug_filial',)

    prepopulated_fields = {'slug': ('filial', 'nome',)}

    search_fields = ['descricao']  # Campo de busca

    # retorna o slug_filial no display
    def slug_filial(self, obj):
        return obj.filial.slug

    def get_queryset(self, request):
        return super(Corredor, self).get_queryset(request).select_related('filial')


@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    fields = ('descricao',)
    list_display = ('descricao',)


@admin.register(Produto)
class Produto(admin.ModelAdmin):
    fields = ('codigo', 'codigo_barras', 'descricao', 'preco_venda', 'categoria', 'slug',)
    list_display = ('id', 'descricao', 'codigo_barras', 'categoria',)

    prepopulated_fields = {'slug': ('codigo', 'descricao',)}


class ConferenciaItensInline(admin.TabularInline):
    list_display = ('conferencia', 'produto', 'quantidade', 'data_validade')
    model = ConferenciaItens
    extra = 0


@admin.register(Conferencia)
class Conferencia(admin.ModelAdmin):
    fields = ('funcionario', 'corredor',)
    list_display = ('id', 'funcionario', 'data_conferencia', 'slug_corredor',)
    inlines = (ConferenciaItensInline,)

    def slug_corredor(self, obj):
        return obj.corredor.slug


@admin.register(Validade_Produto)
class Validade_Produto(admin.ModelAdmin):
    fields = ('conferencia', 'codigo_barras', 'data_validade', 'quantidade',)
    list_display = ('conferencia', 'codigo_barras', 'data_validade',)
