# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


from random import randint
import numpy as np  # Biblioteca 

jogos = int(input('Quantos jogos gerar?\n'))
palpites = np.random.randint(1, 60, (jogos, 6))
print(palpites)
