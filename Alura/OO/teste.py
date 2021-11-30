

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero":numero, "nome": titular, "saldo":saldo, "limite":limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Seu saldo é de {}".format(conta["saldo"]))