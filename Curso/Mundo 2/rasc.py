import time
a = '.'
cont = 0
print(f'Loading', end='')
while True:
    time.sleep(0.3)
    print(f'{a}', end='')
    time.sleep(0.3)
    print(f'{a}', end='')
    time.sleep(0.3)
    print(f'{a}', end='')
    time.sleep(0.3)
    print('\b\b\b', end='')
    cont += 1
    if cont == 3:
        print('\b\b\b\b\b\b\bLoaded')
        break