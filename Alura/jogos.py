import forca
import advinhacao

print("**********************************")
print("**Bem vindo , selecione seu jogo**")
print("**(1) Forca (2) Adivinhação*******")
print("**********************************")

jogo = int(input(":"))

if jogo == 1:
    print("\nAbrindo jogo da forca.\n")
    forca.jogar_forca()
elif jogo == 2:
    print("\nAbrindo jogo de Adivinhação.\n")
    advinhacao.jogar_adv()
else:
    print("\nOpção Invalida.")