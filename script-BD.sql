-- ============================================
-- CRIAÇÃO DO BANCO DE DADOS
-- ============================================
CREATE DATABASE sistema_votacao;
USE sistema_votacao;

/*
drop database sistema_votacao;

drop table if exists voto;
drop table if exists sessao_votacao;
drop table if exists candidato;
drop table if exists eleitor;
*/

-- ============================================
-- TABELA ELEITOR
-- Guarda eleitores e mesários
-- A autenticação usa:
-- titulo_eleitor + cpf_quatro_primeiros + chave_acesso
-- ============================================

CREATE TABLE eleitor (
    id_eleitor INT AUTO_INCREMENT UNIQUE,
    nome_completo VARCHAR(150) NOT NULL,
    cpf VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE,
    titulo_eleitor VARCHAR(20) NOT NULL UNIQUE,
    chave_acesso VARCHAR(255) NOT NULL UNIQUE,
    eh_mesario BOOLEAN NOT NULL DEFAULT FALSE,
    ja_votou BOOLEAN NOT NULL DEFAULT FALSE
    
);

-- inserindo dados de teste

INSERT INTO eleitor
(nome_completo, cpf, titulo_eleitor, chave_acesso, eh_mesario, ja_votou)
VALUES
('Aline Moura Vasconcelos', 'OG4V7QU8A4IT', '538166500191', 'QSHH1HJJS', 0, 0),
('Alex Martins Duarte', 'IFXCWH64W0O4', '422761140116', 'QSHGPIDPG', 0, 0),
('Caio Henrique D’Almeida', '2PQWBH1P36UM', '828734730191', 'H2ECNR2I6', 0, 0),
('Gabriel Monteiro Salles', 'DC3UMQSIG75X', '114145530191', '44M8HSJJS', 0, 0),
('Isabela Ramos Ferreira', 'EYLPTLR75DL8', '322405260124', '5SS1NGUQ2', 0, 0),
('Letícia Carvalho Antunes', 'ZNECPIHFE512', '840750500116', 'P7CEDPJJS', 0, 0),
('Lucas Andrade Moreira', 'EZ9LO4EA1M2O', '143584270183', '3R4TZ5OWQ', 0, 0),
('Lucas Marassi', 'VAZ2IRGMU0EB', '738756400175', '3FSP5GUQ2', TRUE, 0),
('Marina Tavares Coutinho', 'CXG597HB6LDC', '556814660159', 'JOUFMUJJS', 0, 0),
('Noah Oliveira Freitas', 'NSZ3G4BVV0EB', '118430380167', 'JXYI1WZ30', 0, 0),
('Rafael Silveira Prado', 'MO4X9F4IA1PM', '504327160108', 'ZL0CLPZ30', 0, 0);

-- dados de teste descriptografados
/*

CHAVE     CPF          TITULO        NOME COMPLETO
ALM1341   84250242005  538166500191  Aline Moura Vasconcelos
ALM9897   57321400000  422761140116  Alex Martins Duarte
CAH9956   10797595066  828734730191  Caio Henrique D’Almeida
GAM5211   47566620053  114145530191  Gabriel Monteiro Salles
ISR9282   85853433032  322405260124  Isabela Ramos Ferreira
LEC3791   94218158070  840750500116  Letícia Carvalho Antunes
LUA3728   13360701020  143584270183  Lucas Andrade Moreira
LUM3222   23507462087  738756400175  Lucas Marassi
MAT4271   96119810072  556814660159  Marina Tavares Coutinho
NOO9639   43724531087  118430380167  Noah Oliveira Freitas
RAS3379   80051026074  504327160108  Rafael Silveira Prado
*/


-- ============================================
-- TABELA CANDIDATO
-- Guarda candidatos da eleição
-- ============================================

CREATE TABLE candidato (
    id_candidato INT AUTO_INCREMENT UNIQUE,
    nome VARCHAR(150) NOT NULL,
    numero INT PRIMARY KEY NOT NULL UNIQUE,
    partido VARCHAR(50) NOT NULL

);

INSERT INTO candidato (nome, numero, partido) VALUES
('Paulo Henrique Bernardes', 101, 'PDT'),
('Simone Araújo Ferreira', 202, 'PLT'),
('Bruno Cavalcante Ribeiro', 303, 'PRB'),
('Larissa Monteiro da Silva', 404, 'PNS'),
('Thiago Ramos Albuquerque', 505, 'PRT'),
('Renata Gomes Andrade', 606, 'PSD'),
('Eduardo Fontes Cardozo', 707, 'PTB'),
('Viviane Costa Menezes', 808, 'PMC'),
('Henrique Dias Fagundes', 909, 'PRC'),
('Carolina Brito Rezende', 110, 'PVB');

-- ============================================
-- TABELA SESSAO_VOTACAO
-- Controla abertura e encerramento da eleição
-- ============================================

CREATE TABLE sessao_votacao (
    id_sessao INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    aberta BOOLEAN NOT NULL DEFAULT FALSE,
    data_abertura DATETIME NULL,
    data_encerramento DATETIME NULL
);

-- ============================================
-- TABELA VOTO
-- Guarda os votos da eleição
-- id_candidato pode ser NULL para voto nulo
-- ============================================

CREATE TABLE voto (
    id_voto INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    numero_candidato INT NULL,
    id_sessao INT NOT NULL,
    data_hora DATETIME NOT NULL,
    protocolo VARCHAR(255) NOT NULL UNIQUE,


    CONSTRAINT fk_voto_candidato
        FOREIGN KEY (numero_candidato)
        REFERENCES candidato(numero),

    CONSTRAINT fk_voto_sessao
        FOREIGN KEY (id_sessao)
        REFERENCES sessao_votacao(id_sessao)
);


select * from voto;
select * from eleitor order by id_eleitor;
select * from candidato;