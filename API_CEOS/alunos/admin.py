from django.contrib import admin
from .models import Aluno

# Registrando o modelo Aluno no painel de administração do Django
# O decorador @admin.register permite registrar o modelo Aluno na interface administrativa do Django.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso', 'email', 'ano_entrada', 'criacao', 'atualizacao', 'ativo')
    search_fields = ('matricula',)
