print('Bem Vindo a Loja do William')
valor = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com o valor da quantidade: '))
subtotal = valor + quantidade

if 0 <= subtotal < 9:
    desconto = 0.00
    vfinal = subtotal
elif 10 <= subtotal < 99:
    desconto = 0.05
    vfinal = subtotal - subtotal * 0.05
elif 100 <= subtotal < 999:
    desconto = 0.10
    vfinal = subtotal - subtotal * 0.10
else:  # valor for acima de 1000
    vfinal = subtotal - subtotal * 0.15

print('O valor sem desconto: R${:.2f}'.format(subtotal))
print('O valor com desconto: R$ {:.2f} ({:.2f}% de desconto)'.format(vfinal, desconto))
