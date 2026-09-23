import numpy as np
import random
import matplotlib.pyplot as plt

matriz = np.zeros((6, 6), dtype=int)

matriz[0, :] = 1
matriz[5, :] = 1
matriz[:, 0] = 1
matriz[:, 5] = 1

posicao_coluna = 1
posicao_linha = 1

qtde_vezes = random.randint(3, 7)

for _ in range(qtde_vezes):
    linha = random.randint(1, 4)
    coluna = random.randint(1, 4)

    matriz[linha, coluna] = 2

pontos = 0

caminho_atual = []


def funcaoMapear():
    posicao = matriz[posicao_linha, posicao_coluna]

    if posicao == 2:
        sujeira = True
    else:
        sujeira = False

    return [(posicao_coluna, posicao_linha), sujeira]


def checkObj(sala):
    for linha in range(1, 5):
        for coluna in range(1, 5):
            if sala[linha, coluna] == 2:
                return 1

    return 0


def descer():
    global posicao_linha

    if posicao_linha < 4:
        posicao_linha += 1


def subir():
    global posicao_linha

    if posicao_linha > 1:
        posicao_linha -= 1


def moverDireita():
    global posicao_coluna

    if posicao_coluna < 4:
        posicao_coluna += 1


def moverEsquerda():
    global posicao_coluna

    if posicao_coluna > 1:
        posicao_coluna -= 1


def aspirar():
    matriz[posicao_linha, posicao_coluna] = 0


def buscaLargura(inicio, destino):
    fila = [inicio]
    visitados = {inicio}
    anteriores = {}

    while fila:

        atual = fila.pop(0)

        if atual == destino:
            break

        coluna, linha = atual

        vizinhos = [
            (coluna + 1, linha),
            (coluna - 1, linha),
            (coluna, linha + 1),
            (coluna, linha - 1)
        ]

        for vizinho in vizinhos:

            if vizinho in visitados:
                continue

            coluna_vizinho, linha_vizinho = vizinho

            if not (1 <= coluna_vizinho <= 4 and 1 <= linha_vizinho <= 4):
                continue

            visitados.add(vizinho)
            anteriores[vizinho] = atual
            fila.append(vizinho)

    if destino not in visitados:
        return []

    caminho = []
    atual = destino

    while atual != inicio:
        caminho.append(atual)
        atual = anteriores[atual]

    caminho.append(inicio)
    caminho.reverse()

    return caminho


def encontrarSujeiraMaisProxima():
    sujeiras = []

    for linha in range(1, 5):
        for coluna in range(1, 5):
            if matriz[linha, coluna] == 2:
                sujeiras.append((coluna, linha))

    if not sujeiras:
        return None

    menor_caminho = None

    for sujeira in sujeiras:

        caminho = buscaLargura(
            (posicao_coluna, posicao_linha),
            sujeira
        )

        if menor_caminho is None or len(caminho) < len(menor_caminho):
            menor_caminho = caminho

    return menor_caminho


def agenteObjetivo(percepcao, objObtido):

    global pontos, caminho_atual

    if objObtido == 0:
        caminho_atual = []
        return "NoOp"

    posicao, sujeira = percepcao

    if sujeira:
        aspirar()
        pontos += 1
        caminho_atual = []
        return "aspirar"

    if len(caminho_atual) < 2:
        caminho_atual = encontrarSujeiraMaisProxima()

        if caminho_atual is None or len(caminho_atual) < 2:
            caminho_atual = []
            return "NoOp"

    proxima_posicao = caminho_atual[1]

    coluna_atual, linha_atual = posicao
    proxima_coluna, proxima_linha = proxima_posicao

    if proxima_coluna > coluna_atual:
        moverDireita()
        acao = "direita"
    elif proxima_coluna < coluna_atual:
        moverEsquerda()
        acao = "esquerda"
    elif proxima_linha > linha_atual:
        descer()
        acao = "abaixo"
    elif proxima_linha < linha_atual:
        subir()
        acao = "acima"
    else:
        caminho_atual = []
        return "NoOp"

    pontos += 1
    caminho_atual = caminho_atual[1:]

    return acao


cores = [
    'white',
    'orange',
    'black'
]

fig, ax = plt.subplots()

imagem = ax.imshow(
    matriz,
    cmap=plt.cm.colors.ListedColormap(cores)
)

ax.set_xticks(np.arange(-0.5, 6, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 6, 1), minor=True)

ax.grid(
    which='minor',
    color='gray',
    linestyle='-',
    linewidth=1
)

ax.set_xlim(-0.5, 5.5)
ax.set_ylim(5.5, -0.5)

bolinha, = ax.plot(
    [posicao_coluna],
    [posicao_linha],
    'ro',
    markersize=15
)

plt.ion()

while True:

    percepcao = funcaoMapear()

    objObtido = checkObj(matriz)

    acao = agenteObjetivo(percepcao, objObtido)

    imagem.set_data(matriz)

    bolinha.set_data(
        [posicao_coluna],
        [posicao_linha]
    )

    ax.set_title(
        f"Ação: {acao} | Pontos: {pontos}"
    )

    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(1)

    if acao == "NoOp":
        break

for _ in range(6):
    bolinha.set_visible(False)
    ax.set_title(f"Objetivo atingido! | Pontos: {pontos}")
    fig.canvas.draw_idle()
    fig.canvas.flush_events()
    plt.pause(0.3)

    bolinha.set_visible(True)
    fig.canvas.draw_idle()
    fig.canvas.flush_events()
    plt.pause(0.3)

plt.ioff()
plt.show()

print("Objetivo atingido!")
print(f"Total de pontos: {pontos}")