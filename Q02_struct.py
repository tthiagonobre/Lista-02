car = []

for c in range(3):
    print(f'Dados do {c + 1}º carro: ')
    marca = str(input('Insira a marca: '))
    modelo = str(input('Insira o modelo: '))
    ano = int(input('Insira o ano: '))
    dados = {'marca': marca, 'modelo': modelo, 'ano': ano}
    car.append(dados)
print()
print('Dados do carro: ')
for dados in car:
    print(f'Marca: {dados["marca"]}')
    print(f'Modelo: {dados["modelo"]}')
    print(f'Ano: {dados["ano"]}')
    print()