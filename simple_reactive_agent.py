import numpy as np
import random
import matplotlib.pyplot as plt

matriz = np.zeros((6, 6), dtype=int)

matriz[0, :] = 1
matriz[5, :] = 1
matriz[:, 0] = 1
matriz[:, 5] = 1

posicao_coluna = random.randint(1, 4)
posicao_linha = random.randint(1, 4)

qtde_vezes = random.randint(3, 7)

for _ in range(qtde_vezes):
    linha = random.randint(1, 4)
    coluna = random.randint(1, 4)

    matriz[linha, coluna] = 2

voltandoAoInicio = False

def funcaoMapear():
    posicao = matriz[posicao_linha, posicao_coluna]

    if posicao == 2:
        sujeira = True
    else:
        sujeira = False

    return sujeira

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

def movimentarAgente():
    global voltandoAoInicio

    if posicao_linha == 4 and posicao_coluna == 1:
        voltandoAoInicio = True

    if voltandoAoInicio:
        if posicao_linha > 1:
            subir()
        else:
            voltandoAoInicio = False
        return

    if posicao_linha % 2 == 1:
        if posicao_coluna == 4:
            descer()
        else:
            moverDireita()
    else:
        if posicao_coluna == 1:
            descer()
        else:
            moverEsquerda()

def agenteReativoSimples(percepcao):
    sujeira = percepcao

    if sujeira:
        aspirar()
    else:
        movimentarAgente()

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

    agenteReativoSimples(percepcao)

    imagem.set_data(matriz)

    bolinha.set_data(
        [posicao_coluna],
        [posicao_linha]
    )

    fig.canvas.draw_idle()
    fig.canvas.flush_events()

    plt.pause(0.5)