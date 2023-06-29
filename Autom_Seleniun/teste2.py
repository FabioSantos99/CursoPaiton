from random import randint

banca = 10000000
roleta = random.randint(0, 100)
aposta = 200000


if roleta <= 30:
    aposta


elif roleta > 30 and roleta <= 100:
    banca - aposta

else:
     print('Seu saldo acabou')



