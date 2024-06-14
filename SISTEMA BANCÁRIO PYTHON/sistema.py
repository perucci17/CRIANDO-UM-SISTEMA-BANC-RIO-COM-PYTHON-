# Função para exibir o menu
def mostrar_menu():
    print("\nMenu de Opções")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("4. Sair")

# Função para depositar dinheiro
def depositar(saldo, extrato):
    try:
        valor = float(input("Digite o valor para depositar: "))
        if valor <= 0:
            print("Erro: O valor deve ser maior que zero.")
        else:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Erro: Valor inválido. Por favor, digite um número.")
    return saldo, extrato

# Função para sacar dinheiro
def sacar(saldo, extrato, saques_diarios, limite_saque_diario, max_saques_por_dia):
    if saques_diarios >= max_saques_por_dia:
        print("Erro: Número máximo de saques diários atingido.")
        return saldo, extrato, saques_diarios

    try:
        valor = float(input("Digite o valor para sacar: "))
        if valor <= 0:
            print("Erro: O valor deve ser maior que zero.")
        elif valor > saldo:
            print("Erro: Saldo insuficiente.")
        elif valor > limite_saque_diario:
            print(f"Erro: O valor máximo para saque é de R$ {limite_saque_diario:.2f}.")
        else:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Erro: Valor inválido. Por favor, digite um número.")
    
    return saldo, extrato, saques_diarios

# Função para exibir o extrato
def ver_extrato(saldo, extrato):
    print("\nExtrato:")
    if not extrato:
        print("Não foram realizadas transações.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função principal do sistema bancário
def sistema_bancario():
    saldo = 0.0
    extrato = []
    saques_diarios = 0
    max_saques_por_dia = 3
    limite_saque_diario = 500.0

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif escolha == "2":
            saldo, extrato, saques_diarios = sacar(saldo, extrato, saques_diarios, limite_saque_diario, max_saques_por_dia)
        elif escolha == "3":
            ver_extrato(saldo, extrato)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor, tente novamente.")

# Executa o sistema bancário
sistema_bancario()

      

      