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

temp = 0
rete = []
regula = []
#for i in range(0, wiersze):
#    for j in range(0, wiersze):
#        for k in range(0, kolumny):
#            if lista[i][k] != lista[j][k] or i==j:
#                continue
#            elif decyzje[i] != decyzje[j]:
#                break
#            else:
#                print(f"o: {i + 1, j + 1}, a: {k + 1}, d: {decyzje[i], decyzje[j]}")

wynik = []

for i in range(0, wiersze):
    for j in range(0, kolumny):
        for k in range(0, wiersze):
            temp = lista[i][j]
            if decyzje[i] != decyzje[k] and temp == lista[k][j]:
                print('=============================',f'o{i+1} a{j+1}:', lista[i][j],',', f'o{k+1} a{j+1}:',lista[k][j])
                if decyzje[i] != decyzje[k] and temp == lista[k][j]:
                    wynik.clear()
                    rete.clear()
                break
            elif i in regula or k in regula:
                continue
            elif temp == lista[k][j]:
                print(f'o{i+1} a{j+1}:', lista[i][j],',', f'o{k+1} a{j+1}:',lista[k][j])
                wynik.append(f'o{i+1} a{j+1}, o{k+1} a{j+1}: {lista[k][j]}')
                rete.append(k)
        if wynik:
            print(f'(a{j+1}={temp})=>(d={decyzje[i]})[{len(wynik)}]')
            regula += rete
    wynik = []
    rete.clear()

print(regula)