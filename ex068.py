from random import randint
pc = randint(0, 10)
total = 0
print('=-' * 18)
print('Jogue par ou ímpar com o computador')
print('=-' * 18)
while True:
    parimpar = str(input('Par ou Impar [P/I]? ')).strip().upper()
    num = int(input('Escolha um número: '))
    resultado = pc + num
    print('--' * 18)
    print(f'Você jogou {num} e o computador jogou {pc}, o total deu {resultado}.')
    print('--' * 18)
    if parimpar == 'P' and resultado % 2 == 0:
        print('Você GANHOU!!!')
        total += 1
    elif parimpar == 'I' and resultado % 2 != 0:
        print('Você GANHOU!!!')
        total += 1
    else:
        break
    print('Vamos jogar novamente...')
    print('=-' * 18)
print('Você perdeu...')
print(f'Você ganhou {total}x consecutivas.')
