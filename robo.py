from chatterbot import ChatBot

CONFIANCA_MINIMA = 0.70

def iniciar():
    robo = ChatBot("Lua",
        read_only = True,
        logic_adapters = [
            {
                "import_path": "chatterbot.logic.BestMatch"
            }
        ])

    return robo

def executar_robo(robo):
    while True:
        mensagem = input("Digite alguma coisa:  \n")
        resposta = robo.get_response(mensagem.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(">>", resposta.text)
        else:
            print("Infelizmente, ainda não sei responder isso")
            print("Faça outra pergunta: ")

if __name__ == "__main__":
    robo = iniciar()

    executar_robo(robo)