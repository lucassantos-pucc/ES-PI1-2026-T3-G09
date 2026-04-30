# ES-PI1-2026-T3-G09

## DESCRIÇÃO DO PROJETO
Este projeto consiste no desenvolvimento do backend de um sistema de votação
digital fictício, concebido com finalidade estritamente didática. Seu principal objetivo
é promover a integração prática de conhecimentos das áreas de Lógica de
Programação em Python, Manipulação de Bancos de Dados com SQL e aplicação de
conceitos matemáticos (como Álgebra Linear) voltados à proteção da informação.

## NOME DOS INTEGRANTES

- Arthur Gontijo Pace
- Eduardo Monteiro de Castro da Fonseca
- Lucas de Oliveira Santos
- Lucas Marassi Cipriano Pereira
- Lucas Paes Amaro

## TECNOLOGIAS UTILIZADAS

- IDE para desenvolvimento: VSCode
- Linguagem de programação: Python
- Banco de Dados: MySQL
- Repositório: Git com Github
- Gerenciamento do projeto: Github Project
- Criptografia: Cifra de Hill 

## INSTRUÇÕES

Para utilizar o software, é necessário executar o arquivo "script-BD" no seu MySQL instalado localmente.
Em seguida, edite o arquivo "conexao_banco.py" e configure suas credenciais de acesso ao banco de dados.

## ORGANIZAÇÃO E LÓGICA DO PROJETO:

Fluxograma do menu (desatualizado): https://www.canva.com/design/DAHEa11wZ6k/cTQVT0mOsx51UWbOSEnmmg/edit
Fluxograma do novo medu (ainda nao implementado): https://www.canva.com/design/DAHIJxW1Yr4/8hzZ8onuWrnFTequOh2Z0g/edit

O paragrafo abaixo esta desuatalizado, pois o menu sera reformulado no futuro
A pasta src é dividida em três pastas e o arquivo main.py, cada um com seu devido propósito.
O main.py é o ponto de inicial do programa, sendo responsável por inicializar o sistema.
A pasta menus concentra toda a lógica relacionada à interface do usuário, incluindo a exibição de opções, entradas e validação dos dados.
A pasta db reúne funções responsáveis pela interação com o banco de dados MySQL, sendo utilizada pelos menus para validar e armazenar informações.
A pasta conector é responsável por estabelecer a conexão com o banco de dados, sendo utilizada pelos demais arquivos ao longo da execução do programa.

