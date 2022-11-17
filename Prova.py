# Exercicio_1

# lista = []
#
# def CriarLista(a):
#     for i in range(a):
#         lista.append(0 * a)
#     print(lista)
#
#
# n = int(input("Digite o tamanho da lista: "))
# CriarLista(n)
#
# for i in range(n):
#     n1 = int(input("Preencha a lista: "))
#     lista[i] = n1
#
# def soma(lista):
#     s = 0
#     for x in range(len(lista)):
#         s += lista[x]
#     return s
#
# print(f"Letra A {lista}.")
# lista.sort()
# print(f"Letra B {lista}.")
# print(f"Letra C a soma dos valores é {soma(lista)}.")
# for i in range(len(lista)):
#     maior = lista[0]
#     if lista[i] > maior:
#         maior = lista[i]
# print(f"Letra D o maior número da lista é {maior}.")

# Exercicio_2

import random

# dado = [1, 2, 3, 4, 5, 6]
# jogador_1 = []
# jogador_2 = []
# count = soma1 = soma2 = 0
# while True:
#     print('-' * 30)
#     print("[1] Jogar ")
#     print("[2] Sair ")
#     print('-' * 30)
#     r = int(input("Digite uma opção: "))
#     if r == 2:
#         print('FIM DO PROGRAMA!')
#         break
#     elif r == 1:
#         print('-' * 30)
#         print(f"          RODADA {count}")
#         print('-' * 30)
#         if count % 2 == 0:
#             print("É a vez do jogador1.")
#             s = random.randint(0, 5)
#             jogador_1.append(dado[s])
#             print(f"O jogador1 tirou {dado[s]} no dado.")
#             print('-' * 30)
#             count += 1
#         else:
#             print("E a vez do jogador2.")
#             s = random.randint(0, 5)
#             jogador_2.append(dado[s])
#             print(f"O jogador2 tirou {dado[s]} no dado.")
#             print('-' * 30)
#             count += 1
#
# print(f"Jodador 1: {jogador_1}")
# print(f"Jodador 2: {jogador_2}")
# for pos, i in enumerate(jogador_1):
#     soma1 += jogador_1[pos]
# print(f"A soma dos valores do jogador1: {soma1}")
# for pos, i in enumerate(jogador_2):
#     soma2 += jogador_2[pos]
# print(f"A soma dos valores do jogador2: {soma2}")
# if soma1 == soma2:
#     print("EMPATE!")
# elif soma1 > soma2:
#     print("Jogador1 GANHOU!")
#     print("Obrigado por jogar!")
# else:
#     print("Jogador2 GANHOU!")
#     print("Obrigado por jogar!")

# Exercicio_3

# matriz = []
# par = maior = 0
# def Preencher(a, b):
#
#     for i in range(a):
#         matriz.append([0] * b)
#
# linha = int(input("Digite quantas linhas: "))
# coluna = int(input("Digite quantas colunas: "))
# Preencher(linha, coluna)
#
# for l in range(linha):
#     for c in range(coluna):
#         matriz[l][c] = int(input("Digite: "))
#         if matriz[l][c] % 2 == 0:
#             par += matriz[l][c]
#         if l == 0 and c == 0 or matriz[l][c] > maior:
#             maior = matriz[l][c]
# print("Letra A:")
# for pos, x in enumerate(matriz):
#     print(matriz[pos])
# print("Letra B:")
# print(f"A quantidade de números pares são {par}.")
# print("Letra C:")
# print(f"O maior valor da matriz é {maior}.")

# Exercicio_4

# matriz = []
# c = 0
#
# for i in range(5):
#     matriz.append([0] * 5)
#
# for i in range(5):
#     matriz[i][c] = 1
#     c += 1
#
# for pos, x in enumerate(matriz):
#     print(pos, matriz[pos])

#Vinicius Guilherme
