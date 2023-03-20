def media():
    media = (n1 + n2) / 2
    print()
    print(f'A média do aluno {nome} foi: {media}')
    
nome = str(input('Insira o nome: '))
mat = int(input('Insira a matrícula: '))
n1 = float(input('Insira a 1º nota: '))
n2 = float(input('Insira a 2º nota: '))

media()