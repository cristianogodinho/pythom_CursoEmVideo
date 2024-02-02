"""Crie um algoritimo que leia um numero e mostre seu dobro,seu tripo
e a raiz quadrada."""
n = int(input("digite um numero  :"))
d = n * 2
t = n * 3
r = n **(1/2)
print("O dobro de {} é igual à {}".format(n,(n * 2)))
print("O triplo de {} é igual à {}.\nA raiz quadrada de {} é igual à {:.4f}".format(n,t,n,r))


