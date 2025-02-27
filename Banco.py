from time import gmtime, strftime

def withdraw(ammount, balance, withdraw_counter): 

    statement_increment = '' 

    if (ammount <= balance):

        balance -= ammount
        print(f'Operação realizada com sucesso!\nSeu novo saldo é: R$ {balance}')

        withdraw_counter +=1

        statement_increment = (strftime("%d-%m-%Y %H:%M:%S", gmtime())) + f"      SAQUE     R$ {ammount:.2f}\n"

        if withdraw_counter <= 2:    
            print(f'Você ainda pode realizar {WITHDRAW_COUNTER_MAX-withdraw_counter} saques!')

        elif withdraw_counter == 3:
            print(f'Você acaba de atingir o limite de {WITHDRAW_COUNTER_MAX} saques!')

    else:
        print('SALDO INDISPONÍVEL!')

    return balance, withdraw_counter, statement_increment

def check_ammount(operation, ammount):
   
    while True:

        confirmation = int(input(
f'''\n############################################

O valor que você quer {operation} é {ammount}?

[1] - SIM
[2] - NÃO
[0] - CANCELAR

############################################
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

    return ammount, confirmation                        

def deposit(ammount, balance):
    balance += ammount
    print(f'Operação realizada com sucesso!\nSeu novo saldo é: R$ {balance}')
    statement_increment = (strftime("%d-%m-%Y %H:%M:%S", gmtime())) + f"     DEPÓSITO   R$ {ammount:.2f}\n"
    return balance, statement_increment

def statement(balance):
    print(f'Seu saldo é {balance}')
    
WITHDRAW_COUNTER_MAX = 3
WITHDRAW_LIMIT = 500

balance = 0
withdraw_counter = 0

menu = '''
################### MENU ###################
      
Selecione a operação desejada:

[1] - Depositar 
[2] - Sacar 
[3] - Extrato
[0] - Cancelar

############################################
'''

statement = '''
################## EXTRATO ##################

   DATA      HORA       OPERAÇÃO     VALOR
'''

next_operation_text = '''
################### MENU ###################

      DESEJA REALIZAR OUTRA OPERAÇÃO?

[1] - SIM 
[2] - NÃO 

############################################
'''
no_operations = True
date = (strftime("%d-%m-%Y", gmtime()))

while True:
    
    if date != (strftime("%d-%m-%Y", gmtime())):
        date = (strftime("%d-%m-%Y", gmtime()))
        withdraw_counter = 0
    
    previous_balance = balance
    operation = int(input(menu))
    
    if operation == 1:
        
        operation = 'depositar'
        
        print("\nOperação de DEPÓSITO selecionada!\n")
        
        ammount = float(input(f"Forneça o valor que quer {operation}: "))
        
        if ammount <= 0:
            print('Operação falhou! Valor invalido!')
            continue

        ammount, confirmation = check_ammount(operation=operation, ammount=ammount)
        if confirmation == 0:
                continue
        balance, statement_append = deposit(ammount, balance)
        statement += statement_append
        no_operations = bool((previous_balance == balance))

        operation = int(input(next_operation_text))
        while (operation != 1) and (operation != 2):
            print("\nOpção INVÁLIDA! \nTente novamente: ")
            operation = int(input(next_operation_text))
        if operation == 1:
            continue
        else:
            break   
        
    elif operation == 2:
        
        operation = 'sacar'
        
        if withdraw_counter < 3:
            
            print("\nOperação de SAQUE selecionada!\n")
            
            ammount = float(input(f"Forneça o valor que quer {operation}: "))
            
            if ((ammount < 0)):
                print('Operalção falhou! Valor invalido!')
                continue
            elif(ammount > WITHDRAW_LIMIT):
                print(f'O valor excede o seu limite de R$ {WITHDRAW_LIMIT:.2f}!')
                continue

            ammount, confirmation = check_ammount(operation=operation, ammount=ammount)
            if confirmation == 0:
                continue

            balance, withdraw_counter,statement_append = withdraw(ammount, balance, withdraw_counter)
            statement += statement_append
        
        else:
            
            print(f'O limite de {WITHDRAW_COUNTER_MAX} saques já foi atingido!')

        operation = int(input(next_operation_text))
        while operation != 1 and operation != 2:
            print("\nOpção INVÁLIDA! \nTente novamente: ")
            operation = int(input(next_operation_text))
        if operation == 1:
            continue
        else:
            break
    
    elif operation == 3:

        print("\nOperação de VISUALIZAR EXTRATO selecionada!\n")
        if no_operations == True:
            print(f'''################## EXTRATO ##################
                  
    Ainda não foram realizadas operações!
                  
   DATA      HORA       OPERAÇÃO     VALOR                  
---------------------------------------------
{strftime("%d-%m-%Y %H:%M:%S", gmtime())}   SALDO ATUAL  R$ {balance:.2f}
---------------------------------------------

#############################################
''')
        else:           
            print(statement + f'''---------------------------------------------
{strftime("%d-%m-%Y %H:%M:%S", gmtime())}   SALDO ATUAL  R$ {balance:.2f}
---------------------------------------------

#############################################
''')

        operation = int(input(next_operation_text))
        while (operation != 1) and (operation != 2):
            print("\nOpção INVÁLIDA! \nTente novamente: ")
            operation = int(input(next_operation_text))
        if operation == 1:
            continue
        else:
            break 
    
    elif operation == 0:
        
        print("\nOperação de CANCELADA!")
        break
    
    else:
        print("\nOpção INVÁLIDA!")