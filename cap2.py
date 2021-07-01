# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
"""lista = []
for i in range(1, 11):
    x = i
    print(x)
    lista.extend([x])
"""
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
"""
lista = ["red velvet",5,"loona",12,"grupos favs"]
print(lista)
"""
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
"""
str1 = "red"
str2 = " velvet"
str3 = str1+str2
"""
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
"""
tupla = (1,2,2,3,4,4,4,5)
print(tupla.count(4))
"""
# Exercício 5 - Crie um dicionário vazio e imprima na tela
"""
dicio = {

}
print(dicio)
"""
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
"""
dicio = {
    "utt": ["seulgi"],
    "bias": ["yeri","joy"],
    "musica fav": ["little little"]
}
print(dicio)
"""
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
"""dicio = {
    "utt": ["seulgi"],
    "bias": ["yeri","joy"],
    "musica fav": ["little little"]
}
dicio["album"] = "the velvet"
print(dicio)
"""
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
# Imprima o dicionário na tela.
"""loona = {
    "num das bias": [6, 7, 3],
    "solos fav": ["eclipse", "heart attack", "love cherry motion"],
    "bsides favs": ["colors", "fall again", "wow", "stylish"]
}
print(loona)"""
# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
"""dic = {
    "main dancer": "seulgi",
    "main vocalist": "wendy"
}
lista = ["lista",("stream","loona"),dic,4]
print(lista)"""

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
"""
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:19])"""