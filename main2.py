lista = [[1, 1, 1, 1, 3, 1],
         [1, 1, 1, 1, 3, 2],
         [1, 1, 1, 3, 2, 1],
         [1, 1, 1, 3, 3, 2],
         [1, 1, 2, 1, 2, 1],
         [1, 1, 2, 1, 2, 2],
         [1, 1, 2, 2, 3, 1],
         [1, 1, 2, 2, 4, 1]]
decyzje = [1, 1, 0, 1, 0, 1, 0, 1]

wiersze = len(lista)
kolumny = len(lista[0])

rete = []
regula = []
wynik = []

for i in range(0, wiersze):
    for j in range(0, kolumny):
        for k in range(0, wiersze):
            if decyzje[i] != decyzje[k] and lista[i][j] == lista[k][j]:
                wynik.clear()
                rete.clear()
                break
            elif i in regula or k in regula:
                continue
            elif lista[i][j] == lista[k][j]:
                wynik.append(f'o{i+1} a{j+1}, o{k+1} a{j+1}: {lista[k][j]}')
                rete.append(k)
        if wynik:
            print(f'(a{j+1}={lista[i][j]})=>(d={decyzje[i]})[{len(wynik)}]')
            regula += rete
    wynik = []
    rete.clear()
print(regula)

#II	o1  1  1  1  1  3  1  1

#II	o3  1  1  1  3  2  1  0

#II	o5  1  1  2  1  2  1  0

#II	o7  1  1  2  2  3  1  0
