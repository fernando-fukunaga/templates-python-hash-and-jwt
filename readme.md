## Resumo
Este script serve como templete para um fluxo bem simples de autorização com conceitos de oauth2. Ele registra um usuário utilizando o bcrypt para hashear a senha, depois, tenta fazer o login usando a senha normal e conflitando com a senha hasehada do banco de dados usando a função bcrypt.checkpw(). E por fim, se tudo estiver correto, ele gera um token JWT e tenta usá-lo para fazer uma requisição.

A requisição deve retornar um dict com o próprio username do usuário.