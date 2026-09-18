import numpy as np
import matplotlib.pyplot as plt
import random

from matplotlib.colors import ListedColormap

matriz = np.zeros((6, 6), dtype=int)

linhaAgente = random.randint(1, 4)
colunaAgente = random.randint(1, 4)

matriz[0, :] = 1
matriz[-1, :] = 1
matriz[:, 0] = 1
matriz[:, -1] = 1

qtde_vezes = random.randint(1, 15)

for i in range(qtde_vezes):
    linha = random.randint(1, 4)
    coluna = random.randint(1, 4)
    matriz[linha, coluna] = 2

cores = ListedColormap([
    "white",
    "orange",
    "brown"
])

def estaSujo(posicaoX, posicaoY):
    if matriz[posicaoX][posicaoY] == 2:
        return True

    return False

def posicaoValida(posicaoX, posicaoY):

    if (posicaoX >= 1 and posicaoX <= 4) and (posicaoY >= 1 and posicaoY <= 4):
        return True

    return False

def decidirProximaAcao():
    acoesDisponiveis = ["acima", "abaixo", "esquerda", "direita"]
    acaoSorteada = random.choice(acoesDisponiveis)

    return acaoSorteada

def fazerRoboAndar(acao, linha, coluna):
    linhaOriginal = linha 
    colunaOriginal = coluna

    match acao:
        case "acima":
            linha -= 1

        case "abaixo":
            linha += 1

        case "esquerda":
            coluna -= 1

        case "direita":
            coluna += 1

    if posicaoValida(linha, coluna):
            return linha, coluna  

    if linhaOriginal == linha and colunaOriginal == coluna:
        linhaOriginal, colunaOriginal  

    return linhaOriginal, colunaOriginal

def acaoRobo(estaSujo, linhaAgente, colunaAgente, matriz):
    while True:
        if estaSujo(linhaAgente, colunaAgente):
            matriz[linhaAgente, colunaAgente] = 0

        linhaAgente, colunaAgente = fazerRoboAndar(
            decidirProximaAcao(),
            linhaAgente,
            colunaAgente
        )

        imagem.set_data(matriz)
        robo.set_data([colunaAgente], [linhaAgente])

        plt.pause(0.5)

plt.ion()

fig, ax = plt.subplots()

imagem = ax.imshow(matriz, cmap=cores)

ax.set_xticks(np.arange(-0.5, 6, 1), [])
ax.set_yticks(np.arange(-0.5, 6, 1), [])

ax.grid(color="black", linewidth=2)

robo, = ax.plot(
    colunaAgente,
    linhaAgente,
    marker="o",
    color="red",
    markersize=30
)

plt.show(block=False)

acaoRobo(
    estaSujo,
    linhaAgente,
    colunaAgente,
    matriz
)