pessoas = []

for c in range(2):
    print(f'Insira os dados da {c + 1}º pessoa: ')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura (m): '))
    dados = {'nome': nome, 'idade': idade, 'altura': altura}
    pessoas.append(dados)

print('Dados: ')
for dados in pessoas:
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {dados["idade"]}')
    print(f'Altura: {dados["altura"]}')
    