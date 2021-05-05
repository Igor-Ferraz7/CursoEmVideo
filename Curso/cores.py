#• Cores:       •Estilos:
#30 branco     |-0 None
#31 vermelho   |-1 Negrito
#32 verde      |-4 Com linha
#33 amarelo    |-7 Invertido (negative)
#34 azul        •Código:
#35 roxo         \033[estilo;cor;fundom(a string)\033[m
#36 ciano       ex: \033[0;33;44m'Olá mundo\033[m'
#37 cinza
# os.mkdir("C:/Users/User/Desktop/Igor/PYTHON3")
# os.mkdir("C:/Users/User/Desktop/Igor/PYTHON3/obj")
# os.rmdir(("C:/Users/User/Desktop/Igor/PYTHON3"))
branco = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
des = '\033[m'
# while True:
#     try:
#         n = int(input('Nome: '))
#     except ValueError
# def save_obj(obj, name ):
#     with open('C:/Users/User/Desktop/Igor/PYTHON3/obj/' + name + '.txt', 'rt') as f:
#         pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
#
#
# def load_obj(name):
#     with open('obj/' + name + '.txt', 'txt') as f:
#         return pickle.load(f)

def criarq(nome):
    a = open(nome, 'wt+')
    a.close()
def findarq(dic):
    try:
        open(dic, 'wt+')
    except FileNotFoundError:
        criarq(dic)
        print('Arquivo criado.')
    else:
        print('Arquivo ENCONTRADO.')