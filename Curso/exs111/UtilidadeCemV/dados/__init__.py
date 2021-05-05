from exs111.UtilidadeCemV import moeda
def leiadinheiro(n):
    p = input(n).strip().replace(",", ".")
    if p.isalpha() == False and p.find(".") > 0 or p.isnumeric() == True:
        p = float(p)
    if type(p) != float:
        while type(p) != float:
            print(f'Erro! "{p}" não é um número.')
            p = input('Digite o preço novamente: R$').replace(",", ".")
            if p.isalpha() == False and p.find(".") > 0 or p.isnumeric() == True:
                p = float(p)
    if type(p) == float:
        return p
# def leiadinheiro(n):
#     validade = False
#     while not validade:
#         entrada = input(n).strip().replace(',', '.')
#         if entrada.isalpha():
#             print('Erro. Digite o preço nocamentr: R$')
#         else:
#             validade = True
#             return float(entrada)
