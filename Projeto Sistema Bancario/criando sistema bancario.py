menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saque = 1
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        try:

            valor = float(input("Digite o valor do depósito: R$ "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R${valor:.2f}\n"
                print(f"Depósito de R${valor:.2f} realizado com sucesso!")

            else:
                print("Falha na operação: O valor do depósito deve ser positivo.")

        except ValueError:
            print('Falha na operação: Digite valor numérico.')
            continue

    elif opcao.lower() == "s":
        
        try:
            valor = float(input("Digite o valor do saque: R$ "))

            valor_negativo = valor < 0 

            excedeu_limite = valor > LIMITE

            excedeu_saldo = valor > saldo

            excedeu_saque = numero_saque > LIMITE_SAQUE

            if valor_negativo:
                print("Falha na operação: O valor do saque deve ser positivo.")

            elif excedeu_limite:
                print("Falha na operação: O valor é maior que o limite por saque.")
    
            elif excedeu_saldo:
                print("Falha na operação: Saldo insuficiente.")

            elif excedeu_saque:
                print("Falha na operação: Número máximo de saques diário excedido.")
                continue

            else:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saque += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso!")

        except ValueError:
            print('Falha na operação: Digite valor numérico. Tente novamente')
            continue

    elif opcao.lower() == "e":
        print("\n-----------Extrato-------------")
        print()
        print(extrato if extrato else "Nenhuma movimentação registrado.")
        print(f"\nSaldo: R${saldo:.2f}\n")
        print()
        print("\n-------------------------------")

    elif opcao.lower() == "q":
        break

    else:
        print("Falha na operação: Digite a opção cerreta da tela.")