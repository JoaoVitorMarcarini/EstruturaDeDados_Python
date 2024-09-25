# Criando a lista de armaduras do homen de ferro
nome_armaduras = ['Mark IV', 'Mark II', 'Mark III', 'Mark I', 'Mark V']
print('Lista inicial de armaduras', nome_armaduras)

# Adicionando nova armadura ao final da lista
print('\nAdicione uma armadura ao final da lista com o método append')
nome_armaduras.append(input('Digite o nome da nova armadura: '))
print('Lista de armaduras atualizadas', nome_armaduras)

# Adicionando nova armadura em uma posição especifica da lista
print('\nAdicione uma armadura em uma posição especifica da lista com o método insert')
# Mostrando posições disponiveis
print('Posições disponiveis: 0 a', len(nome_armaduras))
nova_armadura = (input('Digite o nome da nova armadura: '))
while True:
    posicao = int(input('Digite a posição que deseja inserir a nova armadura: '))
    if 0 <= posicao <= 6:
        break
    print('Posição invalida! Digite uma posição entre 0 e', len(nome_armaduras))
nome_armaduras.insert(posicao, nova_armadura)
print('Lista de armaduras atualizadas', nome_armaduras)

# Mostrando as armaduras em ordem alfabetica
nome_armaduras.sort()
print('Lista de armaduras em ordem alfabetica: ', nome_armaduras)

# Mostrando em ordem alfabetica ignorando maiúsculo
nome_armaduras.sort(key=str.lower)
print('Lista de armaduras em ordem alfabetica ignorando maiúsculp: ', nome_armaduras)

# Mostrando na ordem alfabetica inversa
nome_armaduras.sort(reverse=True)
print('Lista de armaduras em ordem alfabetica inversa: ', nome_armaduras)

# Criando Tupla da característica das armaduras
print('\nCriando a tupla de característica das armaduras')
print('Digite as características da nova armadura')
caractesticas_armaduras = (
    ('Ferro', 'Pequena', 200),
    ('Titânio', 'Média', 300),
    ('Liga Metálica', 'Média', 400),
    ('Fibra de Carbono', 'Grande', 500),
    ('Ouro', 'Pequena', 600),
    (input('Digite o material da nova armadura: '), input('Digite o tamanho da nova armadura: '),
     input('Digite o peso da nova armadura: '))
)
print('Características das armaduras:', caractesticas_armaduras)

# Contando elementos repetidos na tupla
material = input('\nDigite o material que deseja contar: ')
quantidade = 0
for i in range(len(caractesticas_armaduras)):
    if caractesticas_armaduras[i][0] == material:
        quantidade += 1
print(f'Quantidade de armaduras com o material {material}: {quantidade}')

# Criando o dicionário de informações detalhadas das armaduras
informacoes_armaduras = {
    'Mark I': {'ano': 2008, 'proteção': 'baixa', 'potência de fogo': 10},
    'Mark II': {'ano': 2010, 'proteção': 'média', 'potência de fogo': 20},
    'Mark III': {'ano': 2012, 'proteção': 'média', 'potência de fogo': 30},
    'Mark IV': {'ano': 2013, 'proteção': 'alta', 'potência de fogo': 40},
    'Mark V': {'ano': 2014, 'proteção': 'alta', 'potência de fogo': 50}
}
# Obtendo a lista de tuplas (chave, valor) do dicionário usando o método items()
print('\nObtendo a lista de tuplas (chave, valor) do dicionário usando o método items()')
lista_tuplas = informacoes_armaduras.items()
print(list(lista_tuplas))

# Atualizando informações de uma armadura no dicionário usando o método update()
print('\nAtualizando informações de uma armadura no dicionário usando o método update()')
print('Amaduras disponiveis:', list(informacoes_armaduras.keys()))
armadura = input('Digite o nome da armadura que deseja atualizar as informações: ')
ano = int(input('Digite o ano de lançamento da armadura: '))
protecao = input('Digite o nível de proteção da armadura: ')
potencia = int(input('Digite a potência de fogo da armadura: '))
informacoes_armaduras.update({armadura: {'ano': ano, 'proteção': protecao, 'potencia': potencia}})
print(f'Informações da armadura {armadura} atualizadas: {informacoes_armaduras[armadura]}')

# Removendo uma armadura do dicionário usando o método pop()
print('\nRemovendo uma armadura do dicionário usando o método pop()')
armadura = input(f'Qual armadura você deseja remover {list(informacoes_armaduras.keys())} : ')
informacoes_armaduras.pop(armadura)
print(f'Armadura {armadura} removida do dicionario')
print('Lista de Amaduras atualizadas:', list(informacoes_armaduras.keys()))

# Apresentando o dicionario inteiro
print('\nDicionário de informações das armaduras atualizado:')
for armadura, info in informacoes_armaduras.items():
    print(f'Armadura: {armadura}')
    print('Ano:', info['ano'])
    print('proteção:', info['proteção'])
    print('potência de fogo:', info['potência de fogo'])
    print()
