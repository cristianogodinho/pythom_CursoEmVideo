"""Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
 com 15% de aumento."""
salario=float(input("Digite o seu sálario : R$"))
novo = salario + (salario*15/100)
print("O seu salario de {:.2f} com 15% de reajuste passara a ser de: R${:.2f}".format(salario,novo))