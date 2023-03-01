# API_Escola

___
[Objetivos Gerais do Projeto](#objetivos-gerais-do-projeto)

[Iniciando o Projeto](#iniciando-o-projeto)

[Utilizando o programa através da infertace de Usuário](#utilizando-o-programa-através-da-interface-de-usuário)

[Cadastro de Aluno](#cadastrando-ou-editando-um-aluno)

[Cadastro de Curso](#cadastrando-ou-editando-um-curso)

[Cadastro de Professor](#cadastrando-ou-editando-um-professor)

[Utilizando os Endpoints](#endpoints)

___
## Objetivos gerais do projeto:


* Cadastrar, editar e deletar cursos, professores e alunos;
* Utilizar ferramentas disponíveis no framework Django;
* Disponibilizar endpoints para fazer as solicitações;
* Criar uma interface amigável para usuários que não são familizarizados com o uso de API.

___
## Iniciando o projeto:

Para conseguir utilizar este projeto é pressuposto que você tenha um banco de dados MYSQL com o nome "school_app", utilizando o usuário "root" e senha "admin".

Você pode mudar essas configurações acessando o arquivo "API_Escola/school_api/school_api/settings.py", e modificando a variável "DATABASES".

É necessário também que você possua o framework de Django, e também o Django Rest Framework.

Supridos todos os requisitos anteriores, vá até a pasta "API_Escola/school_api/" e execute o comando ```python manage.py runserver``` para iniciar o servidor.

___
## Utilizando o programa através da interface de usuário

#### HOME

A página está disponível, por padrão, na porta 8000. Para acessá-la abra o seu navegador e digite "http://localhost:8000/"

Isto deve ser o que você verá:

![image](https://user-images.githubusercontent.com/85121830/222183547-2c682769-4d70-4127-801e-e264a455e99e.png)

Existem 7 botões neste página inicial:

* 3 Botões "Cadastrar", que abrirão um modal para o usuário preencher as informações do cadastro que ele escolheu preencher;

* 3 Botões "Consultar", que levarão o usuário à uma página que exibe todos os resultados da opção escolhida;

* 1 Botão "Home", presente na Navbar superior, que será responsável por levar o usuário a página inicial.

#### Modal Cadastrar

Ao clicar em "Cadastrar", o Usuário irá se deparar com um modal, como no exemplo abaixo:

![image](https://user-images.githubusercontent.com/85121830/222184964-52531341-1539-423c-b6d3-0e5046d3819a.png)

Ao preencher as informações corretamente e clicar em "Cadastrar ----", ele irá cadastrar o formulário dentro do banco de dados e receberá uma mensagem de sucesso, como no exemplo abaixo

![image](https://user-images.githubusercontent.com/85121830/222185434-9fdd1779-af2d-4788-8ffb-6333f66f9c4c.png)

#### Página de Consultas

Ao clicar em "Consultar", o usuário será levado à página que exibirá todos os resultados, além de botões para edição e remoção dos registros, como no exemplo abaixo:

![image](https://user-images.githubusercontent.com/85121830/222186471-e891132a-d98a-4aa8-81f5-735afbf60b50.png)


#### Página de Edição

Ao clicar em "Editar", o usuário será levado para uma nova página com as informações do cadastro previamente preenchidas, e será possível modificar o registro selecionado, como no exemplo abaixo:

![image](https://user-images.githubusercontent.com/85121830/222186858-51e3f356-5ed9-4752-a7b3-6b609b5fc592.png)

#### Deletar 

Ao clicar em "Deletar", o registro será extinto, e o usuário verá que a página irá atualizar automaticamente sem o registro apagado.

___
## Cadastrando ou Editando um Aluno 

Ao cadastrar um aluno, será necessário preencher todos os campos a seguir:

* Nome : um campo que recebe até 30 caracteres

* Sobrenome : Um campo que recebe até 50 caracteres

* CPF : Um campo que recebe 14 caracteres no modelo "000.000.000-00". Importante frizar que o CPF deve seguir exatamente o formato proposto, caso haja algum problema no preenchimento, 2 erros podem ser apontados:
  - O primeiro diz respeito à duplicidade de alunos com o mesmo CPF. Ao tentar cadastrar 2 alunos com o mesmo CPF uma mensagem de erro de duplicidade será exibida
  - O segundo diz respeito ao formato. Caso não seja seguido o modelo sugerido, uma mensagem de erro será exibida 

* Email: Um campo de e-mail com validação automática do forms do Django, o que significa que não pode haver um e-mail sem o símbolo de "@", para mais informações consulte a documentação (https://docs.djangoproject.com/en/4.1/ref/forms/fields/).

* UF : Um campo que recebe até 2 caracteres;

* Cidade: Um campo que recebe até 100 caracteres;

* Logradouro: Um campo que recebe até 100 caracteres;

* Número e Complemento: Um campo que recebe até 40 caracteres;

* Data Nascimento: Um campo do tipo Date que deve ser preenchido no formato "DD/MM/AAAA". Ao preencher de forma errada uma mensagem irá aparecer para o usuário, para mais informações consulte a documentação (https://docs.djangoproject.com/en/4.1/ref/forms/fields/);

* Data Matrícula: Um campo do tipo Date que deve ser preenchido no formato "DD/MM/AAAA". Ao preencher de forma errada uma mensagem irá aparecer para o usuário, para mais informações consulte a documentação (https://docs.djangoproject.com/en/4.1/ref/forms/fields/);

*Número Matrícula: Um campo que recebe até 10 caracteres com o placeholder "00000000.0".

___
## Cadastrando ou Editando um Professor

Ao cadastrar um aluno, será necessário preencher todos os campos a seguir:

* Nome : um campo que recebe até 30 caracteres

* Sobrenome : Um campo que recebe até 50 caracteres

* CPF : Um campo que recebe 14 caracteres no modelo "000.000.000-00". Importante frizar que o CPF deve seguir exatamente o formato proposto, caso haja algum problema no preenchimento, 2 erros podem ser apontados:
  - O primeiro diz respeito à duplicidade de alunos com o mesmo CPF. Ao tentar cadastrar 2 alunos com o mesmo CPF uma mensagem de erro de duplicidade será exibida
  - O segundo diz respeito ao formato. Caso não seja seguido o modelo sugerido, uma mensagem de erro será exibida 

* Email: Um campo de e-mail com validação automática do forms do Django, o que significa que não pode haver um e-mail sem o símbolo de "@", para mais informações consulte a documentação (https://docs.djangoproject.com/en/4.1/ref/forms/fields/);

* UF : Um campo que recebe até 2 caracteres;

* Cidade: Um campo que recebe até 100 caracteres;

* Logradouro: Um campo que recebe até 100 caracteres;

* Número e Complemento: Um campo que recebe até 40 caracteres;

* Data Nascimento: Um campo do tipo Date que deve ser preenchido no formato "DD/MM/AAAA". Ao preencher de forma errada uma mensagem irá aparecer para o usuário, para mais informações consulte a documentação (https://docs.djangoproject.com/en/4.1/ref/forms/fields/);

* Data de Contratação: Um campo do tipo Date que deve ser preenchido no formato "DD/MM/AAAA". Ao preencher de forma errada uma mensagem irá aparecer para o usuário, para mais informações consulte a documentação (https://docs.djangoproject.com/en/4.1/ref/forms/fields/);

* Regime de Contratação: Um campo para escolher entre 3 opções pré-selecionadas dentro do modelo "radio select".

___
## Cadastrando ou Editando um Curso

* Nome: um campo que recebe até 100 caracteres;

* Período: Um campo para escolher entre 3 opções pré-selecionadas dentro do modelo "radio select".

___
## Endpoints

A aplicação também disponibiliza 12 (doze) endpoints genéricos para que possa ser utilizada sem a interface:

* Há 3 opções de "listar", que retornarão uma lista no formato JSON, com a opção selecionada, são estes:

  - listar-alunos/ : trás a lista de todos os alunos cadastrados (Método GET)

  - listar-professores/ : trás a lista de todos os professores cadastrados (Método GET)

  - listar-cursos/ : trás a lista de todos os cursos cadastrados (Método GET)

Abaixo está o exemplo de uma solicitação e a resposta obtida com o aplicativo "Postman":

![image](https://user-images.githubusercontent.com/85121830/222196233-6f7b3ce4-50c4-4beb-9866-73b10fc29f9e.png)

* Há 3 opções de "deletar", que retornarão uma resposta de acordo com a solicitação, são estes:

  - 'deletar-aluno/id/: apaga o registro no banco de dados de acordo com o "id" passado (Método DELETE);

  - 'deletar-professor/id/: apaga o registro no banco de dados de acordo com o "id" passado (Método DELETE);

  - 'deletar-curso/id/: apaga o registro no banco de dados de acordo com o "id" passado (Método DELETE);

Abaixo está o exemplo de uma solicitação válida e a resposta obtida com o aplicativo "Postman":

![image](https://user-images.githubusercontent.com/85121830/222197809-75e5b414-3f9c-4b65-b2c5-a3c839e3fc01.png)

Caso o método não seja correto, ou o registro não exista, uma mensagem de erro será retornada.

* Há 3 opções de "editar", que retornarão uma resposta de acordo com a solicitação, são estes:

  - 'editar-aluno/id/: edita o registro no banco de dados de acordo com o "id" passado (Método PUT ou GET);

  - 'editar-professor/id/: edita o registro no banco de dados de acordo com o "id" passado (Método PUT ou GET);

  - 'editar-curso/id/: edita o registro no banco de dados de acordo com o "id" passado (Método PUT ou GET);


Abaixo está o exemplo de uma solicitação válida com o método GET e a resposta obtida com o aplicativo "Postman":

![image](https://user-images.githubusercontent.com/85121830/222199154-354b50cc-8abc-40bc-9514-300ba187b613.png)

E aqui está uma solicitação válida com o método PUT:

![image](https://user-images.githubusercontent.com/85121830/222199394-e79c7fe9-ff0d-492c-adea-58f3bde8478a.png)

Caso o método não seja correto, o registro não exista ou o preenchimento de algum campo esteja incorreto uma mensagem de erro será retornada.

Abaixo estão alguns exemplos de JSON que podem ser enviados para fazer uma edição:


* Curso :
```
{
    "nome": "Matemática II",
    "periodo": "noturno"
}
```
> **Importante**: O período deve ser um destes 3 possíveis: "noturno", "matutino" ou "vespertino". Caso contrário, uma mensagem de erro será retornada.



* Aluno :
```
    {
        "nome": "Priscila",
        "sobrenome": "Silva",
        "cpf": "000.000.000-00",
        "email": "priscila@gmail.com",
        "telefone": "(11)00000-0000",
        "UF": "SP",
        "cidade": "São Paulo",
        "endereco_logradouro": "Rua Alva",
        "endereco_complemento": "número 12",
        "dataNascimento": "2000-01-01",
        "dataMatricula": "2000-01-01",
        "numeroMatricula": "0000000.0"
    }
```
> **Importante**: O CPF deve estar no formato correto (000.000.000-00), as datas devem estar no formato (AAAA-MM-DD). Para mais informações, consulte a seção de [Cadastro de Aluno](#cadastrando-ou-editando-um-aluno).



* Professor :
```
    {
        "nome": "Priscila",
        "sobrenome": "Silva",
        "cpf": "000.000.000-00",
        "email": "priscila@gmail.com",
        "telefone": "(11)00000-0000",
        "UF": "SP",
        "cidade": "São Paulo",
        "endereco_logradouro": "Rua Alva",
        "endereco_complemento": "número 12",
        "dataNascimento": "2000-01-01",
        "dataContratacao": "2000-11-12",
        "regimeContratacao": "clt"
    }
```
> **Importante**: O CPF deve estar no formato correto (000.000.000-00), as datas devem estar no formato (AAAA-MM-DD). Por fim, o campo "regimeContratacao" precisa ter uma das 3 opções ("clt", "PJ", ou "temporario" Para mais informações, consulte a seção de [Cadastro de Professor](#cadastrando-ou-editando-um-professor).

* Por fim, há 3 opções de "cadastrar", que retornarão uma resposta de acordo com a solicitação, são estes:

  - 'cadastrar-aluno/: faz o registro do JSON passado dentro do banco de dados (Método POST);

  - 'cadastrar-professor/: faz o registro do JSON passado dentro do banco de dados (Método POST);

  - 'cadastrar-curso/: faz o registro do JSON passado dentro do banco de dados (Método POST);

Abaixo está o exemplo de uma solicitação válida e a resposta obtida com o aplicativo "Postman":

![image](https://user-images.githubusercontent.com/85121830/222210953-3531266a-1ad4-4e8d-8b71-46104a89a2cb.png)

Caso o método não seja correto ou haja algo errado no preenchimento, uma mensagem de erro será retornada.

Abaixo estão alguns exemplos de JSON que podem ser enviados para fazer uma edição:


* Curso :
```
{
    "nome": "Matemática II",
    "periodo": "noturno"
}
```
> **Importante**: O período deve ser um destes 3 possíveis: "noturno", "matutino" ou "vespertino". Caso contrário, uma mensagem de erro será retornada.


* Aluno :
```
    {
        "nome": "Priscila",
        "sobrenome": "Silva",
        "cpf": "000.000.000-00",
        "email": "priscila@gmail.com",
        "telefone": "(11)00000-0000",
        "UF": "SP",
        "cidade": "São Paulo",
        "endereco_logradouro": "Rua Alva",
        "endereco_complemento": "número 12",
        "dataNascimento": "2000-01-01",
        "dataMatricula": "2000-01-01",
        "numeroMatricula": "0000000.0"
    }
```
> **Importante**: O CPF deve estar no formato correto (000.000.000-00), as datas devem estar no formato (AAAA-MM-DD). Para mais informações, consulte a seção de [Cadastro de Aluno](#cadastrando-ou-editando-um-aluno).



* Professor :
```
    {
        "nome": "Priscila",
        "sobrenome": "Silva",
        "cpf": "000.000.000-00",
        "email": "priscila@gmail.com",
        "telefone": "(11)00000-0000",
        "UF": "SP",
        "cidade": "São Paulo",
        "endereco_logradouro": "Rua Alva",
        "endereco_complemento": "número 12",
        "dataNascimento": "2000-01-01",
        "dataContratacao": "2000-11-12",
        "regimeContratacao": "clt"
    }
```
> **Importante**: O CPF deve estar no formato correto (000.000.000-00), as datas devem estar no formato (AAAA-MM-DD). Por fim, o campo "regimeContratacao" precisa ter uma das 3 opções ("clt", "PJ", ou "temporario" Para mais informações, consulte a seção de [Cadastro de Professor](#cadastrando-ou-editando-um-professor).

