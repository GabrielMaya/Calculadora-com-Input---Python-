# usando o enquanto para quando o usuário digitar um valor maior a estrutura se repetir e pedir um número válido

a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você digitou um valor errado! Informe a nota do primeiro bimestre: '))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Você digitou um valor errado! Informe a nota do primeiro bimestre: '))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('Você digitou um valor errado! Informe a nota do primeiro bimestre: '))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('Você digitou um valor errado! Informe a nota do primeiro bimestre: '))


média = (a + b + c + d) / 4

print('sua média foi: {} ' .format(média))


if média >= 6:
    print('Párabéns você foi aprovado!')
else:
    print('Que pena, você foi reprovado!')






