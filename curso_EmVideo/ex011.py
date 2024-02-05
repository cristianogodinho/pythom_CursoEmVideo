"""Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""
larg=float(input("Largura da Parede:  "))
alt=float(input("Altura da Parede:  "))
area=larg*alt
print("Sua parede tem a dimensão de {} por {} e uma area de :{}m²".format(larg,alt,area))
tinta=area/2
print("Para pintar essa parede voce precisara de {} litros de tinta".format(tinta))
