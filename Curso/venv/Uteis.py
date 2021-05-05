import pickle, os
mydict = {"Hello": 190}
def save_obj(obj, nome):
    with open("C:/Users/User/PycharmProjects/Curso/Mundo 3/meudicpy.py", 'wb') as resumo:
        pickle.dump(obj, resumo, pickle.HIGHEST_PROTOCOL)


# def load_obj(name):
#     with open('C:/Users/User/Desktop/Igor/PYTHON3/obj/' + name + '.pkl', 'rb') as f:
#         return pickle.load(f)


save_obj(mydict, "meudicpy")
