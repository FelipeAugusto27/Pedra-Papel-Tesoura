import random
import time

nome = input("Bem vindo, digite seu nome: ")
print(f"Olá, {nome}!")
print("Escolha o que jogar \n Pedra: 1 \n Papel: 2 \n Tesoura: 3")
jogada = int(input())
if jogada == 1:
    print("Pedra escolhida.")
if jogada == 2:
    print("Papel escolhido.")
if jogada == 3:
    print("Tesoura escolhida.")
print("O oponente escolhe...")
time.sleep(1)
jogadanpc = random.randint(1,3)
if jogadanpc == 1:
    print("O oponente escolheu a pedra.")
elif jogadanpc == 2:
    print("O oponente escolheu o papel.")
elif jogadanpc == 3:
    print("O oponente escolheu a tesoura.")
if jogada == jogadanpc:
    print("Jogadas iguais, tente novamente")
elif (jogada == 1 and jogadanpc == 2) or (jogada == 2 and jogadanpc == 3) or (jogada == 3 and jogadanpc == 1):
    time.sleep(1)
    print("Você perdeu")
elif (jogada == 1 and jogadanpc == 3) or (jogada == 2 and jogadanpc == 1) or (jogada == 3 and jogadanpc == 2):
    time.sleep(1)
    print("Você venceu!")
print("FIM")
