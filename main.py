import numpy as np
import matplotlib.pyplot as plt
import random

from matplotlib.colors import ListedColormap

matriz = np.zeros((6, 6), dtype=int)

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
    "white",   # 0 = limpo
    "orange",  # 1 = parede
    "brown"    # 2 = sujeira
])

plt.imshow(matriz, cmap=cores)

plt.xticks(np.arange(-0.5, 6, 1), [])
plt.yticks(np.arange(-0.5, 6, 1), [])

plt.grid(color="black", linewidth=2)

plt.show()