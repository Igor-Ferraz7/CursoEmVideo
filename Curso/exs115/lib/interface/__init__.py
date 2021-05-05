# coding: iso-8859-1 -*-
import cores
md = {'Macos' : 34, "Igor" : 16}
def criaraqr(nome):
    try:
        a = open(nome)
    except FileNotFoundError:
        a = open(nome, 'wt+')
        print('Arquivo criado.')
    else:
        print('Arquivo encontrado.')
    finally:
        a.close()


def cabeçalho(nm, linha=20):
    print("=-"*linha)
    print(nm.center(40))
    print("=-"*linha)


def cadastro(n=0):
    print(f'{cores.amarelo}1 - {cores.azul}Ver pessoas cadastradas\n'
          f'{cores.amarelo}2 - {cores.azul}Cadastrar uma nova pessoas\n'
          f'{cores.amarelo}3 - {cores.azul}Sair do sistema{cores.des}')


def op(n):
    while True:
        try:
            print('-=' * 20)
            n1 = int(input(f'{cores.verde}{n}{cores.des}')) #poderia colocar para str, porém é necessário treinar os except errors
            if n1 < 1 or n1 > 3:
                a = float(n1 + 'a')
        except (ValueError, TypeError) as erro:
            print(f'{cores.vermelho}Erro. Digite apenas um dos números apresentados.{cores.des}')
            continue
        if n1 == 3:
            break
        else:
            mostrar('meuarquivo', n=n1)


def menu(tt):
    cabeçalho(tt)
    cadastro()
    op(f'Opção{cores.branco}: ')


def add():
    try:
        id = int(input('Idade: '))
    except (ValueError, TypeError) as erro:
        while erro:
            try:
                print('Erro. Digite um número válido.')
                id = int(input('Idade: '))
            except (ValueError, TypeError):
                continue
            else:
                return id
    else:
        return id

def cadastrar(arq, nome='descohecido', id=0):
    a = open(arq, 'at')
    a.write(f'\n{nome}: {id}')
    a.close()
def mostrar(arq, n):
    # print(n)
    if n == 1:
        cabeçalho('Pessoas Cadastradas')
        a = open(arq, 'rt')
        print(a.read())
        a.close()
    if n == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = add()
        cadastrar('meuarquivo', nome, idade)

