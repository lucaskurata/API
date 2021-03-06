# API

O objetivo deste AC é o de desenvolver um sistema de chat simples.
Tanto o lado do cliente quanto o do servidor devem ser desenvolvidos.
O cliente deve ser feito utilizando-se a biblioteca requests e menus em modo texto simples (input e print).
O servidor deve ser feito utilizando-se Flask e SQLite.
Preze pela modularização do código tal como visto em aula.

Cada usuário tem os seguintes campos:
Id: int, nome: str, segredo: str

Cada mensagem tem os seguintes campos:
Id da mensagem: int;
id do remetente: int;
id do destinatário: int; - pode ser 0, para indicar que a mensagem é visível a todos.
data/hora: str - use a biblioteca datetime para validar isso;
texto: str

Os usuários podem se cadastrar por meio da seguinte URL:
POST /usr

O corpo da requisição deve conter um JSON no seguinte formato:
{"nome": <str>}

Se o login já existir, um erro 409 deve ser produzido.
Só serão aceitos usuários vinculados ao LMS,portanto deverá haver o usuário deste chat cadastrado como ALUNO OU PROFESSOR.

A resposta da requisição, se aceita, deve ser um JSON no seguinte formato:
{"id": <int>, "segredo": <str>}
Ambos os campos devem ser gerados pelo servidor.
O campo id é um número sequencial.

Os usuários podem enviar mensagens por meio da seguinte URL:
POST /msg

O corpo da requisição deve conter um JSON no seguinte formato:
{
"de": <int>,
"para": <int>,
"segredo": <str>,
"texto": <str>
}

Se os campos "de" ou "para" referenciarem usuários que não existem, um erro 404 deve ser devolvido. Mais uma vez não esqueça de validar se o usuário existe e se é válido como professor ou aluno...
Se o segredo não for o do usuário do campo "de", um erro 403 deve ser devolvido.
A resposta da requisição, se aceita, deve ser um JSON no seguinte formato:
{"id": <int>, "datahora": <str>}
Ambos os campos devem ser gerados pelo servidor. O id é o id da mensagem e é um número sequencial.

Os usuários podem ler as mensagens postadas por meio da seguinte URL:
GET /msg/<int>?segredo=<str>&inicio=<int>&fim=<int>

Onde:
* inicio é o id da primeira mensagem desejada. É opcional.
* fim é o id da última mensagem desejada. É opcional.
* O <int> da URL é o id do usuário.
* O segredo é o segredo do usuário.

Se o segredo e o id do usuário não coincidirem, um erro 403 deve ser devolvido.

A resposta da requisição, se aceita, deve ser um JSON no seguinte formato:
{"mensagens": [...]}
Cada item das mensagens deve ter o seguinte formato:
{"de": <int>, "para": <int>, "datahora": <str>, "texto": <str>}

Apenas mensagens onde o campo "para" correspondam ao usuário que fez a requisição ou que estejam com zero devem, ser retornadas.

Os usuários podem obter a lista de outros usuários por meio da seguinte URL:
GET /usr

A resposta da requisição, se aceita, deve ser um JSON no seguinte formato:
{"usr": [...]}
Cada item das mensagens deve ter o seguinte formato:
{"id": <int>, "nome": <str>}

Grupos de até 6 pessoas.
