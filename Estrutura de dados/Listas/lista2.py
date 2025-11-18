# métodos

# [].append
# adiciona itens a uma lista
lista = []
lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

print(lista) # [1, 'Python, [40, 30, 20]]

#[].clear
# limpa a lista

lista = [1, 'Python', [40, 30, 20]]
print(lista) # [1, 'Python, [40, 30, 20]]

lista.clear()
print(lista) #[]

# [].copy
# retorna os mesmos valores de uma lista
# mas com uma lista independente que pode ser alterada sem mexer na lista original

# [].count
# conta quantas vezes um elemento aparece em uma lista
cores = ['vermelho', 'azul', 'verde', 'azul']
cores.count('vermelho')
cores.count('azul')
cores.count('verde')

#[].extend
# pega a lista alvo e adiciona todos os elementos que estão no metodo
# no final da lista alvo

linguagens = ['python', 'js', 'c']
print(linguagens)

linguagens.extend(['java', 'csharp'])
print(linguagens)

# [].index
# procura o indice do alvo
# encontra o primeiro indice, caso a palavra se repita
linguagens = ['python', 'js', 'c','java','csharp']
print(linguagens.index('java'))
print(linguagens.index('python'))

# [].pop
# exclui o ultimo item da lista caso não seja informado o indice que será excluido
# se adicionado o indice, será retirado o item na posição

linguagens = ['python', 'js', 'c','java','csharp']
linguagens.pop() # vai retirar o csharp

# também podemos anexar o item retirado em uma nova lista

#[].remove
# esse método é similar ao pop mas ao inves de retirar o último item
# retira o item especificado

linguagens = ['python', 'js', 'c','java','csharp']
print(linguagens.remove(2))

#[].reverse
# vai colocar os itens de trás pra frente na lista
linguagens = ['python', 'js', 'c','java','csharp']
linguagens.reverse()

#[].sort
# faz a ordenação da lista
# ordena alfabéticamente para strings

linguagens = ['python', 'js', 'c','java','csharp']
linguagens.sort()

linguagens = ['python', 'js', 'c','java','csharp']
linguagens.sort(reverse=True)

linguagens = ['python', 'js', 'c','java','csharp']
linguagens.sort(key=lambda x:len(x))

linguagens = ['python', 'js', 'c','java','csharp']
linguagens.sort(key=lambda x: len(x), reverse=True)

# len
# encontra o tamanho da lista

linguagens = ['python', 'js', 'c','java','csharp']
len(linguagens)

# sorted
# função built in usada para ordernar iteráveis

