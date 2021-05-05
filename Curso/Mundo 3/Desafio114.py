from urllib import request

try:
    site = request.urlopen("http://www.pudim.com.br")
except:
    print(f'O site não pode ser acessado no momento.')
else:
    print('O site está acessível no momento.')
