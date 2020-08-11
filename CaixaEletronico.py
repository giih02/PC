import os
import time

def existe_cliente(agenda, email):
    
    agenda = open("agenda", "w")
    if len(agenda) > 0:

        for cliente in agenda:
            if cliente['email'] == email:
                 return True
    return False

def cadastrar():
    agenda = open("agenda", "w")
    n = input('Digite seu nome: ')
    s = input('Digite seu sobrenome: ')
    t = int(input('Digite seu telefone: '))
    e = input('Digite seu email: ')

    agenda = open('agenda','a')
    agenda.write('%s %s, %d, %s\n'%(n, s, t, e))
    agenda.close()

    print("O cliente {} foi cadastrado com sucesso!\n".format(n))

def info():
    n = input('Digite o nome do cliente a ser pesquisado: ' )
    s= input('Digite o sobrenome do cliente a ser pesquisado: ')

    agenda = open('agenda','r')
    busca = agenda.readline()        
    print(busca)
    agenda.close()


def  extrato():
    extratos  = [ 1 , 2 , 3 ]
    input ( "Digite o código de segurança:" )
    print ( " \ n Histórico das operações \ n " )

    for i in ( len ( extratos ), 0 , - 1 ):
        print ( i , "- Valor: 0,00 | Origem: Crédito | Dados: 00/00/0000 00:00:00" )

    input ( " \ n Pressione enter para voltar para o menu" )

def abastecimento():
    
    print("Valor Máximo: 3.039")

    d = input('Digite aqui o valor retirado: ')

    int(d)
    if d == 3039:
        print("Obrigada pela informação. O sistema será reabastecido em alguns minutos")
    elif d <= 2800:
        print("Obrigada pela informação. O sistema deve reabastecer em 15 dias")
    elif d > 3039:
        print("Valor não é válido")
    print("Valor Máximo de Depósito: 3.039")

def movimentacao(): 

    SalarioMinimo =  0
    print('Bem vindo!')
    Nome = str(input('Como devo te chamar?'))
    print('Bom ', Nome, 'antes de começarmos você deve estar ciente que o valor máximo a ser deposita é de 3.039. Logo valores acima desse não serão aceitos.')
    Opt = str(input('Deseja continuar? \n Digite N para NÃO \n  Digite S para SIM\n '))

    if Opt == "N" or Opt== "n": 
        print("Até mais", Nome)
        principal()

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

def administracao(): 

    print('Bem vindo!')
    print("===Administração===")
    print("1 - Cadastrar")
    print("2 - Informação do Cliente")       
    print("3 - Gerenciamento de Abastecimento")
    print("4 - Gerenciamento de Conta")
    print("5 - Sair")
    opcao = int(input("Digite o opção desejada:"))

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        info()
    elif opcao == 3:
        abastecimento()
    elif opcao == 4:
        extrato()
    elif opcao == 5:
        print("Obrigada e Até mais!")
        principal()
    else:
        print("Opcão incorreta, por favor digite novamente...")
        administracao() 

     ## o codigo abaixo está apresentando algum problema cuja dupla não conseguiu resolver  
'''def cliente():
    def existe_cliente(dados, nome):

    dados = open("dados","w")
    if len(dados) > 0:

        for existe_cliente in dados:
            if existe_cliente['nome'] == nome:
                 return True
    return False

def cadastro():

    dados = open("dados", "w"),
    nome = input('Digite o nome do banco: '),
    cnpj = input('Digite o CNPJ: ')

    dados = open('dados','a')
    dados.write('%s %s, %d, %s\n'%(nome,cnpj))
    dados.close()

    print("Parabéns, {} teve o cadastrado realizado!\n".format(nome))

def principal():

    while True:
        time.sleep(2)
        os.system("cls")
        print("*CLIENTE**")
        print("1 - Cadastro")
        print("2 - Alterar ")
        print("3 - Excluir ")
        print("4 - Buscar  ")
        print("5 - Listar  ")
        print("6 - Sair do sistema Banco")
        opcao = int(input("Digite o opção que deseja:"))

        if opcao == 1:
            cadastro()
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
       elif opcao == 5
            pass
        elif opcao == 6:
            print("Saindo do programa, até mais.")
            break
        else:
            print("Não está configura ou é inválida, por favor tente novamente.")
            principal()
      ## o codigo acima está apresentando alguns problemas cuja dupla não conseguiu resolver     ''' 
def principal():
        print("===BANCO DIGITAL===")
        print("1 - Movimentação")
        print("2 - Administração")
        print("3 - Cliente")       
        print("4 - Sair")
        opcao = int(input("Digite o opção desejada:"))

        if opcao == 1:
            movimentacao()
        elif opcao == 2:
            administracao()
        elif opcao == 3:
            cliente()
        elif opcao == 4:
            print("Saindo do programa...")
            print("Obrigada e Até mais!")
            exit()
        else:
            print("Opcão incorreta, por favor digite novamente...")

principal()