# 🎓 API REST - Gerenciamento de Alunos

Este projeto é uma API RESTful simples desenvolvida com **Django** e **Django REST Framework** para gerenciar registros de alunos.

---

## 📌 Funcionalidades

- ✅ Listar todos os alunos (`GET /alunos/`)
- ✅ Cadastrar um novo aluno (`POST /alunos/`)
- ✅ Ver detalhes de um aluno (`GET /alunos/<id>/`)
- ✅ Atualizar dados de um aluno (`PUT /alunos/<id>/`)
- ✅ Deletar um aluno (`DELETE /alunos/<id>/`)
- ✅ Impressão de requisições no terminal (debug)

---

## 🚀 Tecnologias utilizadas

- Python 
- Django 
- Django REST Framework
- SQLite (banco de dados padrão)
- Git & GitHub

---

## Para testar o projeto:
- clone o repositorio
- faça um ambiente virtual e use o comando "pip install -r API_CEOS\requirements.txt" para instalar os pacotes necessarios
- use em sequencia os comandos "python manage.py makemigrations" e "python manage.py migrate" para inicializar o banco de dados
- use o comando "python manage.py runserver" e entre neste link http://127.0.0.1:8000/api/v1/alunos/ para ver a api funcionando
- use o comando "python manage.py test" para rodar os testes da pasta test.py
