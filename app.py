import random

def rolar_dado():
    return random.randint(1, 20)

def responder_mensagem(mensagem):
    if mensagem.lower() == 'rolar':
        resultado = rolar_dado()
        return f"Você rolou um dado e o resultado foi: {resultado}"
    else:
        return "Desculpe, não entendi. Por favor, envie 'rolar' para rolar o dado."

print("Bem-vindo ao Chatbot de Rolagem de Dados!")
print("Envie 'rolar' para rolar um dado.")

while True:
    mensagem = input("Você: ")
    resposta = responder_mensagem(mensagem)
    print("Chatbot: " + resposta)
