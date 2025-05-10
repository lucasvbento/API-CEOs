from django.db import models

#criando modelo base do banco de dados
class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


#Criando modelo de alunos no banco de dados
class Aluno(Base):
    nome = models.CharField(max_length=200)
    matricula = models.IntegerField()
    curso = models.CharField(max_length=200)
    email = models.EmailField()
    ano_entrada = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome

