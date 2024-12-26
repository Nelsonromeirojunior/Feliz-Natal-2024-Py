import numpy as np
import time

x = np.arange(7, 16)
y = np.arange(1, 18, 2)

z = np.column_stack((x[::-1], y))

for i, j in z:
    print(' ' * i + '*' * j)
for _ in range(3):
    print(' ' * 13 + ' | | ')
    print( ' ' * 8 + '\===========/')

def contagem_regressiva():
    print("Contagem Regressiva para o Natal:")
    for i in range(10, 0, -1):
        print(f"{i}...")
        time.sleep(1)
        print("\nFeliz Natal!\nFeliz Navidad!\nMerry Christmas!\nJoyeux Noël!\n")
        print("Desejamos a todos um excelente Natal e um próspero Ano Novo!")
contagem_regressiva()