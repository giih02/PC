def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    valor = 150
    conta['saldo'] -= valor

def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))


conta = cria_conta('7896-9', 'Giovanna Aparecida', 1200.0, 3000.0)
deposita(conta, 400.0)
extrato(conta)
saca(conta, 50.95)
extrato(conta)