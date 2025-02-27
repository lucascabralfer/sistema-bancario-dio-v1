def withdraw(ammount, balance, withdraw_counter): 
    if ammount <= balance:
        balance -= ammount
        print(f'Operação realizada com sucesso!\nSeu novo saldo é: R$ {balance}')
        withdraw_counter +=1
        if withdraw_counter <= 2:    
            print(f'Você ainda pode realizar {WITHDRAW_COUNTER_MAX-withdraw_counter} saques!')
        elif withdraw_counter == 3:
            print(f'Você acaba de atingir o limite de {WITHDRAW_COUNTER_MAX} saques!')
    else:
        print('SALDO INDISPONÍVEL!')
    return balance

def check_ammount(operation, ammount):
    while True:
        confirmation = int(input(
f'''O valor que você quer {operation} é {ammount}?
[1] - SIM
[2] - NÃO
[0] - CANCELAR
'''))
        if confirmation == 1:
             break
        elif confirmation == 2:
            ammount = float(input(f"Forneça o valor que quer {operation}: "))

            while ammount < 0:
                ammount = float(input('Valor invalido! Forneça um novo valor: R$ '))

        elif confirmation == 0:
            print('Operação CANCELADA!\n')
            break
        else:
            print("\nOpção INVÁLIDA! \nTente novamente:")   
    return ammount
                                     

def deposit(ammount, balance):
    balance += ammount
    print(f'Operação realizada com sucesso!\nSeu novo saldo é: R$ {balance}')
    return balance

def statement(balance):
    print(f'Seu saldo é {balance}')
    
WITHDRAW_COUNTER_MAX = 3
WITHDRAW_LIMIT = 500

balance = 0
withdraw_counter = 0

menu = '''
############# MENU ############
      
Selecione a operação desejada:

[1] - Depositar 
[2] - Sacar 
[3] - Extrato
[0] - Cancelar

###############################
'''

statement = '''
############## EXTRATO ###############'''

while True:
    operation = int(input(menu))
    if operation == 1:
        operation = 'depositar'
        print("\nOperação de DEPÓSITO selecionada!\n")
        ammount = float(input(f"Forneça o valor que quer {operation}: "))
        while ammount < 0:
            ammount = float(input('Valor invalido! Forneça um novo valor: R$ '))
        ammount = check_ammount(operation=operation, ammount=ammount)
        balance = deposit(ammount, balance)
    elif operation == 2:
        operation = 'sacar'
        if withdraw_counter <= 3:
            print("\nOperação de SAQUE selecionada!\n")
            ammount = float(input(f"Forneça o valor que quer {operation}: "))
            while ammount < 0:
                ammount = float(input('Valor invalido! Forneça um novo valor: R$ '))
            ammount = check_ammount(operation=operation, ammount=ammount)
            balance = withdraw(ammount, balance, withdraw_counter)
        else:
            print(f'O limite de {WITHDRAW_COUNTER_MAX} saques já foi atingido!')
    elif operation == 3:
        print("\nOperação de VISUALIZAR EXTRATO selecionada!\n")
        print(statement)
    elif operation == 0:
        print("\nOperação de CANCELADA!")
        break
    else:
        print("\nOpção INVÁLIDA! \nTente novamente")