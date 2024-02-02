"""crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
todas as informações possiveis sobre ele:
"""
a = input("Digite algo :")
print('O tipo primitivo desse valor é:',type(a))
print("Só tem espaços?",a.isspace())
print("E´um número?",a.isnumeric())
print("É alfabético:",a.isalpha())
print("É alfanumérico?",a.isalnum())
print("Esta em maiusculas?",a.isupper())
print("Esta em minusculas?",a.islower())
print("Esta capitalizada?",a.istitle())

