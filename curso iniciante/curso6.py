notas = []

while True:
    nota = int(input('Digite uma nota ou -1 para sair: '))
    if nota == -1:
        break
    notas.append(nota)

soma = 0
for i in notas:
    soma = soma + i

print(f" a média da sala é {notas}")
