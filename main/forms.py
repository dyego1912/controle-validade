# from django.forms import ModelForm
from .models import Conferencia, Validade_Produto

from django import forms

# Criação do formulário de conferência

class ConferenciaForm(forms.ModelForm):
    class Meta:
        model = Conferencia
        fields = ['corredor']

        # widgets = {'corredor': forms.TextInput}

class ValidadeProdutoForm(forms.ModelForm):
    class Meta:
        model = Validade_Produto
        # campo conferência vai ser preenchido usando o id da conferência criada
        fields = ['codigo_barras', 'data_validade', 'quantidade']
        widgets = {'codigo_barras': forms.TextInput}

