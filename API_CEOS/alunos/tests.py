from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Aluno


#testes de todas as funçoes da api
class AlunosAPITests(APITestCase):

    def setUp(self):
        self.aluno_data = {
            'nome': 'Lucas Bento',
            'matricula': 12345,
            'curso': 'Ciencia da computaçao',
            'email': 'lucasvbento@teste.com',
            'ano_entrada': 2025.1
        }
        self.url = reverse('alunos')
        self.aluno = Aluno.objects.create(**self.aluno_data)
        self.aluno_url = reverse('aluno', kwargs={'pk': self.aluno.id})

    #teste de listar os alunos
    def test_list_alunos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], self.aluno_data['nome'])

    #teste para criaçao de aluno novo
    def test_create_aluno(self):
        new_aluno_data = {
            'nome': 'Lucas Bento',
            'matricula': 12345,
            'curso': 'Ciencia da computaçao',
            'email': 'lucasvbento@teste.com',
            'ano_entrada': 2025.1
        }
        response = self.client.post(self.url, new_aluno_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        aluno = Aluno.objects.get(matricula=new_aluno_data['matricula'])
        self.assertEqual(aluno.nome, new_aluno_data['nome'])

    #teste para vizualizar um aluno
    def test_get_aluno(self):
        response = self.client.get(self.aluno_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.aluno.nome)

    #teste para atuaizar informaçoes de um aluno
    def test_update_aluno(self):
        updated_data = {
            'nome': 'Lucas Vieira Bento',
            'matricula': self.aluno.matricula,
            'curso': self.aluno.curso,
            'email': self.aluno.email,
            'ano_entrada': self.aluno.ano_entrada
        }
        response = self.client.put(self.aluno_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.nome, 'Lucas Vieira Bento')

    #teste da funçao de deletar um aluno 
    def test_delete_aluno(self):
        response = self.client.delete(self.aluno_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Aluno.DoesNotExist):
            self.aluno.refresh_from_db()
