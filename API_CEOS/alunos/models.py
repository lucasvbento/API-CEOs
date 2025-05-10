from django.db import models

# Criando o modelo base para outras tabelas do banco de dados
# A classe Base define campos comuns para todas as outras classes de modelo, como data de criação, data de atualização e status de ativo.
# Este modelo é abstrato, ou seja, não será usado diretamente no banco de dados, mas sim herdado por outros modelos.
class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


# Criando o modelo de alunos no banco de dados
# A classe Aluno herda de Base, adicionando campos específicos para o registro de alunos.
# Este modelo será utilizado para armazenar informações de alunos no banco de dados.
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

