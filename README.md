# Sistema de Gestão de Competição de Voleibol

Este projeto é um sistema de gestão de competições de voleibol desenvolvido com Flask. O sistema permite o gerenciamento de equipes e chaves, oferecendo uma interface para adicionar e editar essas entidades.

## Funcionalidades

- **Gerenciamento de Equipes**: Adicionar, editar e visualizar equipes.
- **Gerenciamento de Chaves**: Adicionar e remover equipes de chaves, visualizando as chaves e suas respectivas equipes.

## Estrutura do Projeto

- **app.py**: Contém a lógica do Flask e as rotas da aplicação.
- **db.py**: Responsável pela conexão com o banco de dados e pelas operações CRUD.
- **Templates**: Arquivos HTML para a interface do usuário.
- **Static**: Arquivos estáticos como CSS e imagens.

## Divisão dos arquivos
- ┏ Static
- ┣  - fluxograma.jpeg
- ┗  - styles.css
- ┏ Template
- ┣  - chaves.html
- ┣  - editar_chave.html
- ┣  - equipes.html
- ┣  - equipes_chave.html
- ┣  - form_chave.html
- ┗  - form_equipe.html
- ┏  README.md
- ┣  app.py
- ┗  db.py

## Fluxograma

O fluxograma abaixo ilustra a arquitetura e o fluxo de dados do sistema:

![Fluxograma](static/fluxograma.jpeg)
