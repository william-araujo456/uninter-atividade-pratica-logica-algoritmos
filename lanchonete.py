acumulador = 0
print('BEM VINDO A LANCHONETE DO WILLIAM MATTSON')

print('===============CARDÁPIO===============')
print('[CÓDIGO]    [DESCRIÇÃO]            [VALOR]')
print('[100]    Cachorro-Quente          [R$9,00]')
print('[101]    Cachorro-Quente Duplo   [R$11,00]')
print('[102]    X-Egg                   [R$12,00]')
print('[103]    X-Salada                [R$13,00]')
print('[104]    X-Bacon                 [R$14,00]')
print('[105]    X-Tudo                  [R$17,00]')
print('[200]    Refrigerante Lata        [R$5,00]')
print('[201]    Chá Gelado               [R$4,00]')

while True:
    cod = input('Entre com o Código desejado:')
    if cod == "100":
        acumulador = acumulador + 9
    elif cod == "101":
        acumulador = acumulador + 11
    elif cod == "102":
        acumulador = acumulador + 12
    elif cod == "103":
        acumulador = acumulador + 13
    elif cod == "104":
        acumulador = acumulador + 14
    elif cod == "105":
        acumulador = acumulador + 17
    elif cod == "200":
        acumulador = acumulador + 5
    elif cod == "201":
        acumulador = acumulador + 4
    else:
        print('Opção inválida')
        continue
    resposta = input('Deseja pedir mais alguma coisa? (S/N)')
    if resposta == 'S':
        continue
    else:
        print('O total a ser pago é: {:.2f}'.format(acumulador))
        break
