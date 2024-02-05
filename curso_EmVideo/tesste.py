saldo=int(input("digite um valor bancario R$:  "))
saque=int(input("digite o valor do saque R$:  "))
if saldo >= saque:
    saldo = saldo - saque
    print("saque realizado com sucesso")
else:
    print("Você não possui saldo suficiente para realizar essa operação")