lista = [[1, 1, 1, 1, 3, 1],
         [1, 1, 1, 1, 3, 2],
         [1, 1, 1, 3, 2, 1],
         [1, 1, 1, 3, 3, 2],
         [1, 1, 2, 1, 2, 1],
         [1, 1, 2, 1, 2, 2],
         [1, 1, 2, 2, 3, 1],
         [1, 1, 2, 2, 4, 1]]
decyzje = [[1], [1], [0], [1], [0], [1], [0], [1]]

wiersze = len(lista)
kolumny = len(lista[0])

temp = 0

#for i in range(0, wiersze):
#    for j in range(0, wiersze):
#        for k in range(0, kolumny):
#            if lista[i][k] != lista[j][k] or i==j:
#                continue
#            elif decyzje[i] != decyzje[j]:
#                break
#            else:
#                print(f"o: {i + 1, j + 1}, a: {k + 1}, d: {decyzje[i], decyzje[j]}")

for i in range(0, wiersze):
    for j in range(0, wiersze):
        for k in range(0, kolumny):
            temp = lista[i][k]