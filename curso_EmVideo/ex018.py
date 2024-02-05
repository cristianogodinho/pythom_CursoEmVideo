"""Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela
 o valor do seno, cosseno e tangente desse ângulo."""
import math
angulo=float(input('digite um angulo :'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O angulo de {} tem o seno de {:.4f}".format(angulo,seno))
print("O angulo de {} tem o cosseno de {:.4f}".format(angulo,cosseno))
print("O angulo de {} tem a tangente de {:.4f}".format(angulo,tangente))
