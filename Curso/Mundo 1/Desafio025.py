n = str(input('Digite seu nome:'))
fd = n.find('Silva')
if fd == -1:
    print('Seu nome não contém Silva.')
elif fd != 1:
    print('Seu nome contém Silva.')