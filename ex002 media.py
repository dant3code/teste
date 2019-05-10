n1 = float (input('Informe sua media do primeiro bimestre: '))
print ('Sua primeira nota é: ', n1)
n2 = float (input('Informe sua media do segundo bimestre: '))
print ('Sua segunda nota é: ', n2)
n3 = float (input('Informe sua media do terceiro bimestre: '))
print ('Sua terceira nota é: ', n3)
n4 = float (input('Informa sua media do quarto bimestre: '))
print ('Sua terceira nota é: ', n4)
media = (n1 + n2 + n3 + n4) / 4

print ('Sua media total é: ', media)

if media >= 5.5:
    print ('APROVADO')
else: print ('REPROVADO')
