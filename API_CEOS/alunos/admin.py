from django.contrib import admin
from .models import Aluno

#criando o objeto aluno no admin do django
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso', 'email', 'ano_entrada', 'criacao', 'atualizacao', 'ativo')
    search_fields = ('matricula',)
