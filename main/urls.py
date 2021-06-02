# Importa o módulo path
from django.urls import path

# import o arquivo de views
from . import views

app_name = 'main'

urlpatterns = [
    # path("produtos/", views.produto_list, name='lista_produtos'),
    # path("produtos/<slug:slug>/", views.produto_detalhes, name='detalhes_produtos'),
    # path('login/', views.login_pagina, name='login_pagina'),
    path('', views.index, name='index'),
    path("conferencias/", views.conferencia_list, name='lista_conferencia'),
    path("conferencias/<int:id>/", views.detalhes_conferencia, name='detalhes_conferencia'),    
    path("nova-conferencia/", views.nova_conferencia, name='nova_conferencia'),
    path("nova-conferencia-itens/", views.nova_conferecia_itens, name='nova_conferencia_itens'),    
]

