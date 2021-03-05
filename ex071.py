logo = 'BANCO DANTAS'
print('=' * 24)
print(f'{logo:^24}')
print('=' * 24)
while True:
    valor = int(input('Que valor você deseja sacar? R$'))
    if valor < 10:
        unidade = valor
        print(f'Total de {unidade} cédulas de R$1.')
        break
    elif 20 > valor >= 10:
        dezena = valor // 10
        unidade = valor - 10
        if unidade > 0:
            print(f'Total de {dezena} cédulas de R$10.')
            print(f'Total de {unidade} cédulas de R$1.')
        if unidade == 0:
            print(f'Total de {dezena} cédulas de R$10.')
        break
    elif 50 > valor >= 20:
        vinte = valor // 20
        dezena = valor % 20 // 10
        unidade = valor % 10
        if valor % 20 == 0:
            print(f'Total de {vinte} cédulas de R$20.')
        elif dezena == 0:
            print(f'Total de {vinte} cédulas de R$20.')
            print(f'Total de {unidade} cédulas de R$1.')
        elif unidade == 0:
            print(f'Total de {vinte} cédulas de R$20.')
            print(f'Total de {dezena} cédulas de R$10.')
        else:
            print(f'Total de {vinte} cédulas de R$20.')
            print(f'Total de {dezena} cédulas de R$10.')
            print(f'Total de {unidade} cédulas de R$1.')

        break
    else:
        cinquenta = valor // 50
        vinte = valor % 50 // 20
        dezena = valor % 50 % 20 // 10
        unidade = valor % 50 % 20 % 10
        if valor % 50 == 0:
            print(f'Total de {cinquenta} cédulas de R$50.')
        elif vinte == 0 and dezena == 0:
            print(f'Total de {cinquenta} cédulas de R$50.')
            print(f'Total de {unidade} cédulas de R$1.')
        elif vinte == 0 and unidade == 0:
            print(f'Total de {cinquenta} cédulas de R$50.')
            print(f'Total de {dezena} cédulas de R$10.')
        elif dezena == 0 and unidade == 0:
            print(f'Total de {cinquenta} cédulas de R$50.')
            print(f'Total de {vinte} cédulas de R$20.')
        elif vinte == 0:
            print(f'Total de {cinquenta} cédulas de R$50.')
            print(f'Total de {dezena} cédulas de R$10.')
            print(f'Total de {unidade} cédulas de R$1.')
        elif dezena == 0:
            print(f'Total de {cinquenta} cédulas de R$50.')
            print(f'Total de {vinte} cédulas de R$20.')
            print(f'Total de {unidade} cédulas de R$1.')
        else:
            print(f'Total de {cinquenta} cédulas de R$50.')
            print(f'Total de {vinte} cédulas de R$20.')
            print(f'Total de {dezena} cédulas de R$10.')
            print(f'Total de {unidade} cédulas de R$1.')
        break
print('=' * 24)
print('Volte sempre ao Banco Dantas. Tenha um bom dia! :)')
