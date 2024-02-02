"""Escreva um programa que leia um valor em metros e o exiba
convertido em centimetros e milimetros."""
"""conversor de medidas."""
medida=float(input('uma distancia em metros  :'))
cm = medida * 100
mm = medida * 1000
print("A medida de {} corresponde à {} cm e {} mm".format(medida,cm,mm))
