lista = [1, 2, 3]
idx = 1
soma = 0
for num in lista:
    print("Jogador", idx, num)
    idx = idx + 1
    soma = soma + num
print(soma)

media = soma / round(len(lista))
print(media)