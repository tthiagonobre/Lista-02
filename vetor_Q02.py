vet = []

for cont in range(0, 10):
    vet.append(int(input(f'Digite um valor na posição {cont}: ')))
vet.sort(reverse = True)   
print(f'vetor na ordem reversa: {vet}')
