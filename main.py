import forca
import adivinhacao

print("Escolha o jogo que deseja jogar: \n")
print("(1) Forca")
print("(2) Adivinhação")

while True:
    escolha = input("Escolha: ")

    if int(escolha) == 1:
        forca.jogar()
        break
    elif int(escolha) == 2:
        adivinhacao.jogar()
        break
    else:
        print("Digite 1 ou 2.")
