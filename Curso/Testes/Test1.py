# coding: iso-8859-1 -*-
import pickle
def save(obj, nome):
    with open('C:/Users/User/PycharmProjects/Curso/exs115/' + nome + '.txt', 'wt') as arq:
        pickle.dump(obj, arq)


dit = ['Igor', "31"]
atest = open('C:/Users/User/PycharmProjects/Curso/exs115/meuarquivo', 'wt')
atest.writelines(dit)
