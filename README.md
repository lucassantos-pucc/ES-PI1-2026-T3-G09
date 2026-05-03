# ES-PI1-2026-T3-G09

---

## DESCRIÇÃO DO PROJETO
Este projeto consiste no desenvolvimento do backend de um sistema de votação digital fictício, criado exclusivamente para fins didáticos. Seu principal objetivo é integrar conhecimentos de:

- Lógica de Programação em **Python**
- Manipulação de Banco de Dados em **SQL**
- Aplicação de conceitos matemáticos (como **Álgebra Linear**) para proteção da informação

---

## NOME DOS INTEGRANTES

- Arthur Gontijo Pace
- Eduardo Monteiro de Castro da Fonseca
- Lucas de Oliveira Santos
- Lucas Marassi Cipriano Pereira
- Lucas Paes Amaro

---

## TECNOLOGIAS UTILIZADAS

- IDE para desenvolvimento: VSCode
- Linguagem de programação: Python
- Banco de Dados: MySQL
- Repositório: Git com Github
- Gerenciamento do projeto: Github Project
- Criptografia: Cifra de Hill 

---

## INSTRUÇÕES
1. Execute o arquivo **`script-BD`** no seu MySQL local para criar o banco de dados.  
2. Configure o arquivo **`conexao_banco.py`** com suas credenciais de acesso ao banco.

---

## ORGANIZAÇÃO E LÓGICA DO PROJETO

### Fluxogramas
- Fluxograma do menu (desatualizado):  
  https://www.canva.com/design/DAHEa11wZ6k/cTQVT0mOsx51UWbOSEnmmg/edit

- Fluxograma do novo menu (ainda não implementado):  
  https://www.canva.com/design/DAHIJxW1Yr4/8hzZ8onuWrnFTequOh2Z0g/edit

---

## Estrutura de Pastas 

> **Observação:** As informações abaixo ainda estão desatualizadas, pois o menu será reformulado futuramente.

<p>A pasta src é organizada em três subpastas e um arquivo principal, cada um com uma função específica dentro do sistema:</p>

- main.py: é o ponto de entrada da aplicação, responsável por iniciar o programa e coordenar sua execução.
- menus: contém toda a lógica da interface com o usuário, incluindo exibição de opções, coleta de entradas e validação dos dados informados.
- db: reúne as funções responsáveis pela interação com o banco de dados MySQL, sendo utilizada pelos módulos de menu para consultar, validar e armazenar informações.
- conector: encarrega-se de estabelecer e gerenciar a conexão com o banco de dados, servindo de suporte para os demais módulos durante a execução do sistema.
