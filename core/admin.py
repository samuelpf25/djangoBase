from django.contrib import admin

from .models import Cargo, Servico, Equipe, RecursosEsquerda, RecursosDireita, ContatoModel, ProdutosModel

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo','modificado')

@admin.register(RecursosEsquerda)
class RecursoEsquerdaAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'descricao', 'icone')

@admin.register(RecursosDireita)
class RecursoDireitaAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'descricao', 'icone')

@admin.register(ContatoModel)
class ContatoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(ProdutosModel)
class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade', 'preco')

