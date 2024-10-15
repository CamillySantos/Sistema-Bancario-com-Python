menu = """

Seja bem-vindx ao banco!

[0] Saldo
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Informe o numero da operação que deseja realizar: """

saldo = 0
extrato = ''
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3


while True:
    
    opcao = input(menu)
    
    if opcao == '0':
      
        print(f'Seu saldo é de R${saldo}')
    
    elif opcao == '1':
        
        print('\nVocê escolheu a opção de depósito!')
        
        while True:
            
            valor = int(input('Selecione o valor que deseja depositar: R$'))
        
            if valor > 0:
                saldo += valor
                extrato += f'Deposito R${valor}\n'
                print(f'\nDeposito realizado com sucesso! Seu saldo atual é de R${saldo}')
                
                break
            
            else:
                print('\nOperação falhou! Informe outro valor.')
                
    elif opcao == '2':
        
        print('\nVocê escolheu a opção saque!')
        
        while True:
                
            valor = int(input('Informe o valor que deseja sacar: R$'))
                
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saque >= LIMITE_SAQUE

                
            if excedeu_saldo:
                print('Operação falhou! Saldo insuficiênte.')
                    
            elif excedeu_limite:
                print('Operação falhou! Excedeu o limite, por favor tente novamente ')
                
            elif excedeu_saques:
                print('Operação falhou! Número máximo de saques excedido.')
                break
                    
            elif valor > 0:
                    
                saldo -= valor
                extrato += f'Saque R${valor}\n'
                print(f'Saque realizado com sucesso! Seu saldo atual é de R${saldo}')
                numero_saque += 1
                    
                break
                
        else:
            print('Limite de tentativas atingido!\nTente novamente amanhã')
                
        
    elif opcao == '3':
        print('\n====================== EXTRATO ========================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo R$ {saldo:.2f}')
        print('=======================================================')
        
    elif opcao == '4':
        print('Até logo! Agradecemos por usar nosso banco!')
        break
        
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')