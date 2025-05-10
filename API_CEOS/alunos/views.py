from rest_framework import generics
from .models import Aluno
from .serializers import AlunoSerializer


#View com funçao GET e POST
class AlunosAPIView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer  
    

    def get(self, request, *args, **kwargs):
        #Printar requisiçoes como pedido
        print(f"[GET] Listando alunos - {request.method} {request.path}")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(f"[POST] Criando aluno - Dados recebidos: {request.data}")
        return super().post(request, *args, **kwargs)



#View com funçao PUT , DELETE e GET
class AlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    
    def get(self, request, *args, **kwargs):
        print(f"[GET] Detalhe do aluno ID={kwargs.get('pk')}")
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print(f"[PUT] Atualizando aluno ID={kwargs.get('pk')} - Dados: {request.data}")
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print(f"[DELETE] Removendo aluno ID={kwargs.get('pk')}")
        return super().delete(request, *args, **kwargs)