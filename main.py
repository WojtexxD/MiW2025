lista = [[1, 1, 1, 1, 3, 1],
         [1, 1, 1, 1, 3, 2],
         [1, 1, 1, 3, 2, 1],
         [1, 1, 1, 3, 3, 2],
         [1, 1, 2, 1, 2, 1],
         [1, 1, 2, 1, 2, 2],
         [1, 1, 2, 2, 3, 1],
         [1, 1, 2, 2, 4, 1]]
decyzje = [[1], [1], [0], [1], [0], [1], [0], [1]]

wiersze=len(lista)
kolumny=len(lista[0])

temp=0

for i in range(kolumny):

    for j in range(wiersze):
        if lista[temp][i] == lista[j][i] and decyzje[temp] == decyzje[j] and temp != j:
            print(f"o{temp+1}, a{i+1}")
            print(f"o{j+1}, a{i+1}")
        elif decyzje[temp] != decyzje[j]:
            break