import win32com.client as win32


# criar integração com o outlook
gmail = win32.Dispatch('outlook.application')

email = gmail.CreateItem(0)

faturamento = 1500
qtde_produtos = 10
ticket_medio = faturamento / qtde_produtos


# configurar informações do email

email.To = "fsantos93x@gmail.com; belarminoleitefrancisco@gmail.com"
email.Subject = "O FalsoE-mail automático do Python do Pix"
email.HTMLBody = f"""
<p>Olá Fabio, aqui é codigo Python</p>

<p>O faturamento da loja foi de R${faturamento}</p>
<p>Vendemos {qtde_produtos} produtos</p> 
<p>O ticket Médio foi de {ticket_medio}</p>

<p>ABS,</p>
<p>Código Python</p>
"""

anexo = r"C:\Users\fsant\Pictures\jaulinha.webp"
email.Attachments.Add(anexo)

email.Send()
print("Email enviado")
