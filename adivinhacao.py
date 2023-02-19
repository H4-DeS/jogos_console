import random


def jogar():
    print("*****************************************")
    print("************Jogo de Adivinhação**********")
    print("*****************************************")

    numero_secreto = int(random.random() * 100)
    chances = 10

    while chances > 0:
        print("Você tem {} chances.\n".format(chances))
        while True:
            chute = input("Tente adivinhar o número secreto: ")
            chute = int(chute)
            if 0 <= chute <= 100:
                break
            else:
                print("Você precisa digitar um valor no intervalo de 0 a 100.")

        if chute > numero_secreto:
            print("O seu chute foi maior que o número secreto!")
            chances -= 1
            continue
        elif chute < numero_secreto:
            print("O seu chute foi menor que o número secreto!")
            chances -= 1
            continue
        else:
            print("Parabéns, você acertou, o número secreto era {}.".format(numero_secreto))
            break
    if chances == 0:
        print("Game Over. \n Suas Chances acabaram.")


if __name__ == "__main__":
    jogar()
