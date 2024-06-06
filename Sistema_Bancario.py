menu = """

Qual operação deseja executar? 
D - Deposito 
S - Saque
E - Extrato 
Q - Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "D":
        nDeposito = float(input("Digite o valor do deposito: " ))
        if nDeposito <= 0:
            print("Valor não pode ser menor ou igual a 0, tente novamente ")
        else:
            saldo = saldo + nDeposito
            extrato += f""" saldo de R$ {saldo}, após o depósito de R$ {nDeposito}\n """

    elif opcao == "S":
        nSaque = float(input("Digite o valor do Saque:" ))

        if LIMITE_SAQUE == numero_saque:
            print("Não é possivel sacar mais que 3 vezes e o limite maximo é 500 por saque ")

        if numero_saque > LIMITE_SAQUE:
                print("O limite maximo é 500 por saque ")

        if saldo < nSaque:
            print("Não é possivel sacar o dinheiro por falta de saldo")    
        
        if saldo > nSaque:
            saldo -= nSaque
            numero_saque += 1
            extrato += f""" saldo de R$ {saldo}, após o saque de R$ {nSaque}\n """

    elif opcao == "E":
        print("---------Extrato---------")
        print("Não foram realizadas movimentações." if not extrato else extrato )
        print(f"saldo R$ {saldo}")

    elif opcao == "Q":
        print("Sair")
        break
    else:
        print("Função não executada")
    
