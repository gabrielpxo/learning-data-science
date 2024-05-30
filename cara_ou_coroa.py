import random
from collections import Counter

# Definir o espaço amostral para uma moeda
espaco_amostral = ['cara', 'coroa']

# Número de lançamentos da moeda
num_lancamentos = 10000

# Simular lançamentos da moeda
lancamentos = [random.choice(espaco_amostral) for _ in range(num_lancamentos)]
# random.choice(): escolhe aleatoriamente um item do conjunto espaco_amostral
# for _ in range(): isso acontecerá pelo numero de vezes definido em num_lancamentos
# lancamentos: será o conjunto de itens definidos ao acaso pela função random.choice() de tamanho num_lancamentos

# Contar a frequência de cada resultado
frequencias = Counter(lancamentos)
# Counter: cria um dicionário em que as chaves são os elementos do conjunto e os valores são as contagens desses elementos
# o dicionário ficará armazenado em 'frequencias'
# exemplo de output: frequencias = [{'cara': 4999, 'coroa': 5001}] 
# dicionario = [{'chave': valor}]

# Calcular a probabilidade de cada resultado
probabilidades = {resultado: frequencia / num_lancamentos for resultado, frequencia in frequencias.items()}
# aqui utiliza-se dados do dicionário 'frequencias' para definir a probabilidade de cada chave, criando-se o novo dicionário 'probabilidades'
# a probabilidade de cada resultado é igual ao número de vezes que apareceu dividido pela quantidade de lançamentos
# convenientemente, o número de aparições já foi revelado pela função Counter
# então, para cada resultado (que é a chave), utilizaremos a frequencia (que é o valor) para calcular sua probabilidade


# Exibir as probabilidades
print("Probabilidades de cada resultado no lançamento de uma moeda:")
for resultado, probabilidade in probabilidades.items():
    print(f"Resultado {resultado}: {probabilidade:.2%}")
# aqui definimos no dicionário 'probabilidades' que resultado é chave e probabilidade é valor
# entao para cada item, teremos a impressão dos dados
