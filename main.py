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

for _ in range(qtde_vezes):
    linha = random.randint(1, 4)
    coluna = random.randint(1, 4)
    matriz[linha, coluna] = 2

cores = ListedColormap([
    "white",
    "orange",
    "brown"
])

def estaSujo(posicaoX, posicaoY):
    return matriz[posicaoX][posicaoY] == 2

def posicaoValida(posicaoX, posicaoY):
    return 1 <= posicaoX <= 4 and 1 <= posicaoY <= 4

def decidirProximaAcao():
    acoesDisponiveis = ["acima", "abaixo", "esquerda", "direita"]
    return random.choice(acoesDisponiveis)

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

    return linhaOriginal, colunaOriginal

def soltarConfete():
    quantidade = 250

    x = np.random.uniform(-0.5, 5.5, quantidade)
    y = np.random.uniform(-2.5, -0.2, quantidade)

    velocidadeX = np.random.uniform(-0.05, 0.05, quantidade)
    velocidadeY = np.random.uniform(0.02, 0.12, quantidade)

    gravidade = 0.004
    coresConfete = np.random.rand(quantidade)
    tamanhos = np.random.uniform(20, 80, quantidade)

    confetes = ax.scatter(
        x,
        y,
        c=coresConfete,
        cmap="hsv",
        s=tamanhos,
        marker="s",
        zorder=5
    )

    ax.set_title("Tudo limpo!", fontsize=18)

    for _ in range(180):
        velocidadeY += gravidade
        x += velocidadeX
        y += velocidadeY

        confetes.set_offsets(np.column_stack((x, y)))
        plt.pause(0.02)

def acaoRobo(linhaAgente, colunaAgente, matriz):
    while True:
        if estaSujo(linhaAgente, colunaAgente):
            matriz[linhaAgente, colunaAgente] = 0

        imagem.set_data(matriz)
        robo.set_data([colunaAgente], [linhaAgente])
        plt.pause(0.2)

        if not np.any(matriz == 2):
            soltarConfete()
            break

        linhaAgente, colunaAgente = fazerRoboAndar(
            decidirProximaAcao(),
            linhaAgente,
            colunaAgente
        )

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
    markersize=20,
    zorder=6
)

plt.show(block=False)

acaoRobo(
    linhaAgente,
    colunaAgente,
    matriz
)

plt.ioff()
plt.show()