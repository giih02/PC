SalarioMinimo =  0
print('Bem vindo!')
Nome = str(input('Como devo te chamar?'))
print('Bom ', Nome, 'antes de começarmos você deve estar ciente que o valor máximo a ser deposita é de 3.039. Logo valores acima desse não serão aceitos.')
Opt = str(input('Deseja continuar? \n Digite N para NÃO \n  Digite S para SIM '))

if Opt == "N" or Opt== "n": 
    print("Até mais", Nome)
    exit()

print('[1] 1- 1.031 \n[2] 2- 2.062 \n[3] 3- 3.093\n')
Sal = int(input(' quantos salários mínimos você ganha?')) 

if Sal == 1: 
    SalarioMinimo = 1031
if Sal == 2:
    SalarioMinimo = 2062
if Sal == 3: 
    SalarioMinimo = 3039

print('Entre com a opção desejada: ')
print('[1] Pagamento \n[2] Saque \n[3] Deposito \n[4] Sair')
opc = int(input('Entre com a opção desejada: '))


while opc != 4:
    if opc == 1:
        print('A opção selecionada foi [1] Pagamento de contas')
        NomeConta = str(input('Qual a conta ou boleto será pago a seguir?'))
        ValorConta = int(input('Qual o valor dessa conta ou boleto? '))
        if ValorConta > SalarioMinimo: 
            print("Saldo insuficiente")
        else: 
            sobra = SalarioMinimo-ValorConta
            print(Nome, 'a sua ',NomeConta, ' no valor de ', ValorConta, ' foi paga com sucesso. \n Saldo atual: R$ ', sobra, ',00')
    if opc == 2:
        print('A opção selecionada foi [2] saque')
        ValorConta = int(input('Qual o valor do saque? '))
        if ValorConta > SalarioMinimo: 
            print("Saldo insuficiente")
        else: 
            sobra = SalarioMinimo-ValorConta
            print(Nome, 'a sua ',NomeConta, ' no valor de ', ValorConta, ' foi paga com sucesso. \n Saldo atual: R$ ', sobra, ',00')
    if opc == 3:
        print('A opção selecionada foi [3] depósito')
        NomeConta = str(input('Qual a conta que será depositada?'))
        ValorConta = int(input('Qual o valor a ser depositado? '))
        if ValorConta > SalarioMinimo: 
            print("Saldo insuficiente")
        else: 
            sobra = SalarioMinimo-ValorConta
            print(Nome, 'a sua ',NomeConta, ' no valor de ', ValorConta, ' foi paga com sucesso. \n Saldo atual: R$ ', sobra, ',00')