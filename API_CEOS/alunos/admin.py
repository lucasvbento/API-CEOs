from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso', 'email', 'ano_entrada', 'criacao', 'atualizacao', 'ativo')
    search_fields = ('matricula',)
