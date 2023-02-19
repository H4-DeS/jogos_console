import random


def imprime_abertura():
    print("\n\n          *****************************************")
    print("          ************Jogo da Forca****************")
    print("          *****************************************\n\n")

    print("|x|x|x|x|x|x|x|                            ")
    print("|x|          |                             ")
    print("|x|                                        ")
    print("|x|                                        ")
    print("|x|                                        ")
    print("|x|                                        ")
    print("|x|______________________                  \n")


def sorteia_palavra():
    palavras = []
    arquivo = open("palavras.txt", "r")

    for palavra in arquivo:
        palavras.append(palavra.split())

    arquivo.close()

    index_random = random.randrange(0, len(palavras))
    palavra_secreta = ''.join(palavras[index_random])
    palavra_secreta = palavra_secreta.upper()
    return palavra_secreta


def inicializa_campos_resposta(palavra_secreta):
    return ["__" for letra in palavra_secreta]


def define_dificuldade():
    print("\nEscolha a dificuldade: ")
    print("\n(1) Fácil")
    print("\n(2) Médio")
    print("\n(3) Difícil")
    while True:
        escolha = int(input("Escolha: "))
        if escolha == 1:
            return 15
        elif escolha == 2:
            return 10
        elif escolha == 3:
            return 5
        else:
            print("\nEscolha inválida.")


def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_forca(tentativas):

    print("  _______     ")
    print(" |/      |    ")

    if (tentativas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    imprime_abertura()
    palavra_secreta = sorteia_palavra()
    resposta = inicializa_campos_resposta(palavra_secreta)
    #tentativas = define_dificuldade()
    tentativas = 7
    for letra in resposta:
        print(letra, end=" ")

    while "__" in resposta and tentativas > 0:

        chute = input("\nChute uma letra: ").upper()
        acertou = False
        for index in range(0, len(palavra_secreta)):
            if palavra_secreta[index] == chute:
                resposta[index] = chute
                acertou = True

        if not acertou:
            tentativas -= 1
            imprime_forca(tentativas)
        for letra in resposta:
            print(letra, end=" ")

    if tentativas == 0:
        imprime_mensagem_derrota(palavra_secreta)
    elif tentativas > 0:
        imprime_mensagem_vitoria()


if __name__ == "__main__":
    jogar()
