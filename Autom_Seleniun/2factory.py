import time
import pyotp
# import qrcode

print (pyotp.random.base32)

# chave_mestre = "fgergfbewfdberrWWFRWeew346sd"
#
# codigo = pyotp.TOTP(chave_mestre)
# print(codigo.now())
#
# # codigo_usuario = input("Código: ")
# # print(codigo.verify(codigo_usuario))
#
# link = pyotp.TOTP(chave_mestre).provisioning_uri(name='Fabio', issuer_name="CodigoPython")
# print(link)
# meu_qrcode = qrcode.make(link)
# meu_qrcode.save("qrcode.png")
