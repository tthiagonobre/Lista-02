def aumento(nome, salario):
    novo_salario = salario * 1.1
    return novo_salario
    
nome = str(input('Insira o nome: '))
salario = float(input('Digite o salário: '))
novo_salario = aumento(nome, salario)
print(f'Salário de {nome} com 10% de aumento: {novo_salario}')
