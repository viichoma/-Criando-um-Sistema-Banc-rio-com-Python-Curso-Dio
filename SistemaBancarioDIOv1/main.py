MENU = """
[D] DEPOSITAR
[S] SACAR
[E] EXTRATO
[Q] SAIR
"""

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE = 500

while 1:
    opcao = (input(MENU)).upper()
    match opcao:
        case "D":
            valor = float(input("Digite o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"R$ {valor:.2f} depositados.")

            else:
                print("Valor informado inválido.")

        case "S":
            valor = float(input("Digite o valor do saque: "))

            if valor > saldo:
                print("Saldo insuficiente.")

            elif valor > LIMITE:
                print("O valor de saque excedeu o limite.")

            elif numero_saques > LIMITE_SAQUES:
                print("Número de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"R$ {valor:.2f} sacados.")

            else:
                print("Valor inválido.")

        case "E":
            print("\n[------------------EXTRATO------------------]")
            if extrato:
                print(extrato, end="")
            else:
                print("Não foram realizadas movimentações.", end="")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("[-------------------------------------------]")
        case "Q":
            break
        case _:
            print("\nOperação inválida. Selecione uma das opções do menu.")