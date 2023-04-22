nota1 = int(input("digite a nota: "))
nota2 = int(input("digite a nota: "))
nota3 = int(input("digite a nota: "))

frequencia = int(input("Sua frequencia:"))


media = (nota1 + nota2 + nota3) / 3

if media >= 6 or frequencia >= 60:
    print('Você foi aprovado')

else:
    print('Você foi reprovado')







