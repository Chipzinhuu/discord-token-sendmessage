import requests

print ("Olá, muito obrigado por usar meu progama!")
print ("Para alguma dúvida o discord do criador é (._emmxkz) ")
print ("")
entrada_token = input("Insira o token da conta: ")

token = entrada_token
canal_id = input("Insira o ID do canal: ")

headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

print("\nEnvie mensagens abaixo. Feche o programa para encerrar.\n")
print("")

while True:
    mensagem = input("Mensagem: ")

    url = f"https://discord.com/api/v9/channels/{canal_id}/messages"
    data = {
        "content": mensagem
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code in (200, 201):
        print("✅ Mensagem enviada!")
    else:
        print(f" Erro {response.status_code}: {response.text}")