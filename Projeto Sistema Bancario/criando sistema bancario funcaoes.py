import textwrap

def menu() -> None:
    menu = """\n
    ================MENU================\n
    [d]\t Depositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar conta
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def sacar(*,saldo: float, valor: float, extrato: str, limite: int, 
          numeros_saques: int, limite_saques: int) -> float | str:
    valor_negativo = valor < 0 

    excedeu_limite = valor > limite

    excedeu_saldo = valor > saldo

    excedeu_saque = numeros_saques > limite_saques

    if valor_negativo:
        print("@@@Falha na operação: O valor do saque deve ser positivo.@@@")
        return saldo, numeros_saques, extrato
    
    elif excedeu_limite:
        print("@@@Falha na operação: O valor é maior que o limite por saque.@@@")
        return saldo, numeros_saques, extrato
    
    elif excedeu_saldo:
        print("@@@Falha na operação: Saldo insuficiente.@@@")
        return saldo, numeros_saques, extrato
    
    elif excedeu_saque:
        print("@@@Falha na operação: Número máximo de saques diário excedido.@@@")
        return saldo, numeros_saques, extrato

    else:
        saldo -= valor
        extrato += f"Saque:\tR${valor:.2f}\n"
        numeros_saques += 1
        print(f"===Saque de R${valor:.2f} realizado com sucesso!===")
        return saldo, numeros_saques, extrato
    
def depositar(saldo: float, extrato: str, valor:float, /) -> float | str:
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print(f"===Depósito de R${valor:.2f} realizado com sucesso!===")
    
    else:
        print("@@@Falha na operação: O valor do depósito deve ser positivo.@@@")

    return saldo, extrato
    
def extrair_extrato(saldo,/,*, extrato) -> None:

    print("\n-----------Extrato-------------")
    print()
    print(extrato if extrato else "\tNenhuma movimentação registrado.")
    print(f"\nSaldo:\tR${saldo:.2f}\n")
    print("\n-------------------------------")

def novo_usuario(usuarios:list) -> None:
    cpf = input('Informe o CPF (Somente númmeros): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('@@@Cliente já cadastrado!@@@')
        return
    
    nome = input('Informe o nome completo: ' )
    data_de_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ' )
    logradouro = input('Informe o logradouro: ' )
    numero_redencial = input('Informe o número da residência: ' )
    bairro = input('Informe o bairro: ' )
    cidade = input('Informe a cidade: ' )
    estado_sigla = input('Informe o Estado (Sigla), ex: SP, SC, BA...: ' )
    endereco =f'{logradouro},{numero_redencial} - {bairro} - {cidade}/{estado_sigla}'

    cliente_novo = {
            'cpf': cpf,
            'nome': nome,
            'data_de_nascimento': data_de_nascimento,
            'endereco': endereco
            }
    
    usuarios.append(cliente_novo)
    print('===Usuário cadastrado com sucesso!===')

def filtrar_usuarios(cpf:str, usuarios:list) -> str | None:
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia:str, numero_conta: int, 
                     contas: list, usuarios: list) -> None:

    if not usuarios:
        print('@@@Não há clientes cadastrados no cadastro, fluxo de criação encerrada.@@@')
        return
    
    cpf = input('Informe o CPF (Somente númmeros): ')
    usuario = filtrar_usuarios(cpf, usuarios)


    if usuario:
        print('===Conta criada com sucesso!===')
        cadastro_conta = {'agencia':agencia,'numero_conta': numero_conta, 'usuario': usuario}
        contas.append(cadastro_conta)
        
    else:
        print(f'@@@Usuário não encontrado, fluxo de criação encerrada.@@@')

def lista_conta(contas: list) -> None:
    for conta in contas:
        if conta:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
                """
            print("=" * 100)
            print(textwrap.dedent(linha))
        else: 
            print('@@@Não há conta para listar@@@')

def main():
    saldo = 0
    LIMITE = 500
    extrato = ""
    numeros_saques = 1
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = '0001'

    while True:

        opcao = menu()

        if opcao.lower() == "d":
            try:

                valor = float(input("Digite o valor do depósito: R$ "))

            except ValueError:
                print('Falha na operação: Digite valor numérico.')
                continue
            
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao.lower() == "s":
        
            try:
                valor = float(input("Digite o valor do saque: R$ "))

            except ValueError:
                print('Falha na operação: Digite valor numérico. Tente novamente')
                continue

            saldo, numeros_saques, extrato = sacar(saldo = saldo, 
                                                valor = valor, 
                                                extrato = extrato, 
                                                limite = LIMITE, 
                                                numeros_saques = numeros_saques, 
                                                limite_saques = LIMITE_SAQUES
                                                )

        elif opcao.lower() == "e":
            extrair_extrato(saldo, extrato = extrato)

        elif opcao.lower() == "nu":
            novo_usuario(usuarios)

        elif opcao.lower() == "nc":
            numero_conta = len(numero_conta+1)
            nova_conta(AGENCIA, numero_conta, 
                                contas, usuarios) 
    
        elif opcao.lower() == "lc":

            lista_conta(contas)
        
        elif opcao.lower() == "q":
            break

        else:
            print("Falha na operação: Digite a opção cerreta da tela.")


main()