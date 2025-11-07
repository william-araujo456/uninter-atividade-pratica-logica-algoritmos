listaPecas = []


# Começo cadastrarPeca
def cadastrarPeca(codigo):
    print('Bem Vindo ao CADASTRAR peças')
    codigo = int(input('O CÓDIGO da peça a ser cadastrada é:'.format(codigo)))
    nome = input('Digite o NOME da peça:')
    fabricante = input('Digite a FABRICANTE:')
    valor = input('Digite o VALOR da peça:')
    dicionarioPeca = {'Codigo': codigo,
                      'Nome': nome,
                      'Fabricante': fabricante,
                      'Valor': valor}
    listaPecas.append(dicionarioPeca.copy())


# Fim cadastrarPeca

# Começo consultarPeca
def consultarPeca():
    while True:
        try:
            print('Bem Vindo ao CONSULTAR peças')
            opConsulta = int(input('Entre com a opção desejada:\n'
                                   '1- Consultar TODAS as peças\n'
                                   '2- Consultar por CÓDIGO\n'
                                   '3- Consultar por FABRICANTE\n'
                                   '4- Retornar\n'
                                   '>>'))
            if opConsulta == 1:
                print('Você selecionou constultar TODAS as peças')
                for peca in listaPecas:
                    for key, value in peca.items():
                        print('{}:{}'.format(key, value))
            elif opConsulta == 2:
                print('Você selecionou consultar por CÓDIGO')
                entrada = int(input('Digite o CÓDIGO desejado:'))
                for peca in listaPecas:
                    if (peca['Codigo'] == entrada):
                        for key, value in peca.items():
                            print('{}:{}'.format(key, value))
            elif opConsulta == 3:
                print('Você selecionou consultar por FABRICANTE')
                entrada = input('Digite a FABRICANTE desejado:')
                for peca in listaPecas:
                    if (peca['Fabricante'] == entrada):
                        for key, value in peca.items():
                            print('{}:{}'.format(key, value))
            elif opConsulta == 4:
                break
            else:
                print('Opção inválida!')
                continue
        except ValueError:
            print('Pare de digitar valores não inteiros!')


# Fim consultarPeca

# Começo removerPeca
def removerPeca():
    print('Bem Vindo ao REMOVER peças')
    entrada = int(input('Digite o CÓDIGO desejado:'))
    for peca in listaPecas:
        if (peca['codigo'] == entrada):
            listaPecas.remove(peca)


# Fim removerPeca

# Comeco MAIN
print('Bem Vindo ao Controle de Estoque da Bicicletaria do William Mattson')
registroPeca = 0
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n'
                          '1- Cadastrar Peças\n'
                          '2- Consultar Peças\n'
                          '3- Rmover Peças\n'
                          '4- Sair'
                          '\n>>'))
        if opcao == 1:
            registroPeca = registroPeca + 1
            cadastrarPeca(registroPeca)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Finalizando Programa...')
            break
        else:
            print('Opção inválida!')
            continue
    except ValueError:
        print('Pare de digitar valores não inteiros!')
# Fim MAIN
