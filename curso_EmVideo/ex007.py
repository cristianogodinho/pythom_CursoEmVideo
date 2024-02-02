"""crie um programa que leia duas notas de um aluno,
calcule e mostre sua média."""
nota1 = float(input("Primeira nota do aluno  :"))
nota2 = float(input("Segunda nota do aluno  :"))
média = float(nota1+nota2)/2
print("A média entre a nota {:.1f} e à nota {:.1f} é igual à nota : {:.1f}".format(nota1,nota2,média))



