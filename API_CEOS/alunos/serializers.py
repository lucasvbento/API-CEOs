from rest_framework import serializers
from .models import Aluno

# Serializador para o modelo Aluno
# A classe AlunoSerializer transforma os dados do modelo Aluno em formatos como JSON ou XML, e vice-versa.
# Esse serializador é usado para validar, criar e atualizar instâncias de Aluno através da API.
class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        # 'write_only': True significa que o campo 'email' será usado apenas para escrita (entrada de dados), 
        # mas não será incluído na resposta (retorno de dados).
        extra_kwagrs = {
            'email': {'write_only': True}
        }
        model = Aluno

        # Definindo os campos que serão incluídos na serialização e na deserialização.
        # Esses campos são os que o Django REST Framework irá converter em JSON ao receber ou retornar dados.
        fields = (
            'id',
            'nome',
            'matricula',
            'curso',
            'email',
            'ano_entrada'
        )
    
