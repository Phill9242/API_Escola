# API_Escola

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

Supridos todos os requisitos anteriores, vá até a pasta "API_Escola/school_api/" e execute o comando "python manage.py runserver" para iniciar o servidor.

___
## Utilizando o programa através da interface

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




