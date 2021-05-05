l = str(input('Digite o nome de uma cidade:')).strip()
lr = l.split()
if lr[0] == 'Santo':
    print('Sua cidade possui "Santo" no primeiro nome.')
elif lr[0] != 'Santo':
    print('Sua cidade não possui "Santo" no primeiro nome.')