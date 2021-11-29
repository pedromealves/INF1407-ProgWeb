# INF1407-ProgWeb

## Grupo

- João Marcello Bessa Rodrigues - 1720539
- Pedro Afonso Menezes Alves - 1713049

## Funcionalidades

- Implementação de CRUD - OK
- Implementação de Login/Registro - OK
- Visões exlusivas do site para cada usuário - OK
- Implementação de AJAX - OK
- Publicação do site em um provedor de serviço Web - OK

## Desenvolvimento

Desenvolvemos um site para criar, exibir, alterar e deletar reservas de um hotel. 

O desenvolvimento do site começou pela implementação de CRUD. A página para exibir reservas foi desenvolvida e testada através da página admin padrão do django. Posteriormente, foram adicionadas as páginas para criar, deletar e alterar uma reserva.

Em sequência, adicionamos as funcionalidades de login e registro de usuário, assim como a funcionalidade que permite que cada usuário tenha visões exclusivas de reservas efetuadas.

Por fim, adicionamos uma funcionalidade referente a AJAX em que, caso um usuário crie uma reserva para entrar e sair no mesmo dia e horário, ele será alertado pela página até que realize a alteração pedida. Essa funcionalidade pode ser conferida na página de criação ou alteração de uma reserva. Logo após isso, adicionamos estilo nas páginas e configuramos o projeto para colocá-lo no Heroku.

## Funcionamento do Site

Ao acessar o site, através da URL ou rodando localmente, temos a tela de login de início. Para usuários que já possuem conta, basta acessar colocando o nome de usuário no campo "Username" e a senha no campo "Password" para ser redirecionado para a página com as reservas efetuadas. Caso contrário, o usuário precisará criar uma conta e para isso deve clicar no botão "Criar conta" e acessar a página de registro.

Na página de registro, o usuário necessitará escolher um nome de usuário, inseri-lo no campo "Username" e escolher uma senha que se adeque às regras definidas. Após a escolha e verificação da senha, basta clicar no botão "Register" que a criação da conta será confirmada e o redirecionamento para a página com as reservas efetuadas será realizado.

Na página com uma lista de reservas efetuadas, é possível realizar a criação de uma nova reserva clicando no botão "Criar nova reserva". Nessa criação, é necessário inserir uma data e hora de entrada e a data e hora de saída da reserva, sendo os campos preenchidos no padrão conforme solicitado. Finalizando o preenchimento, o usuário será redirecionado para a página principal com a(s) reserva(s) requerida(s). De volta à tela inicial e com a lista de reservas populadas, é possível observar algumas funções que podem ser realizadas sobre as reservas realizadas. A primeira função, que consta o ícone de um lápis, é a de edição de uma reserva, na qual o usuário pode editar as datas e horas da reserva solicitada. A segunda função é a de deletar a mesma, excluindo-a da lista. Além disso, uma funcionalidade muito útil para uma lista com muitas reservas é a busca por uma reserva específica, onde será necessário inserir a data de entrada no formato adequado e clicar no botão "search" para verificar detalhes da reserva.

Por fim, para o usuário se deslogar do site, basta clicar no botão "Logout" que será a sessão será encerrada e o usuário será redirecionado para a tela de Login.
