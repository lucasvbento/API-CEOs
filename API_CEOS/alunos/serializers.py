from rest_framework import serializers
from .models import Aluno

class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwagrs = {
            'email': {'write_only': True}
        }
        model = Aluno
        fields = (
            'id',
            'nome',
            'matricula',
            'curso',
            'email',
            'ano_entrada'
        )
    
