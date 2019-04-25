# GOODRINK - PROJETO MINI-TWITTER

### DESCRIÇÃO
Implementar uma API REST em que um usuário possa realizar um cadastro, publicar Posts e ver as publicações de outros usuários.


### REQUISITOS TÉCNICOS
- Python 3
- Django
- Django REST Framework

### CASOS DE USO

- **CASO 1 - Cadastro de usuário:** O ator faz o cadastro no sistema através da API.

- **CASO 2 -  Autenticação (Login):** O ator deve ser autenticado no sistema através de um Token.

- **CASO 3 - Fazer um Post:** O ator cria um post. Este Post é persistido no sistema.
    - Restrições: O usuário deve estar autenticado para fazer o Post.

- **CASO 4 - Feed:** O ator deve receber, no formato JSON, o feed dos últimos 10 posts.
    - Restrições: O usuário não deve ver os próprios Posts.
