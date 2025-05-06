from django.urls import path
from .views import AlunosAPIView, AlunoAPIView

urlpatterns = [
    path('alunos/', AlunosAPIView.as_view(), name='alunos'),
    path('alunos/<int:pk>', AlunoAPIView.as_view(), name='aluno')
    

]
