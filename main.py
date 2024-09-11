print ("Seja bem vindo ao Banco Premier!")

saldo = 2000
deposito1 = 150
print(f"deposito1 {deposito1:,.2f}")
deposito2 = 200
print(f"deposito2 {deposito2:,.2f}")
limite_saque = 500
saque = 600


def deposito (entrada):
      print (f"Você recebeu um depósito de {entrada} ")
    
def limite_valor_saque (saida):
    
    if saida > limite_saque:
        print (f"Você atingiu o limite de depósito diário de {limite_saque}")
    
def calcular_soma (deposito1,deposito2):
    return deposito1+deposito2
    
def exibir_extrato (saldo,deposito1,deposito2,saque):
    print (f"Seu saldo atual é de {saldo+deposito1+deposito2}")
    
deposito (deposito1)
deposito (deposito2)
limite_valor_saque (saque)
exibir_extrato (saldo,deposito1,deposito2,saque)