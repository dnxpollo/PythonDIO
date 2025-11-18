# set
# uma coleção que não possui objetos repetidos
# o conjunto elimina os elementos duplicados
# funciona com iteraveis
 
linguagens = {'python', 'java', 'python'}
print(set(linguagens))

# para poder acessar os itens de um conjunto
# é necessário transforma-lo em uma lista
# após isso conseguimos acessar os indices

# Metodos
# {}.union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)

# {}.intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b)

# {}.difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)

# {}.symmetric_difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b)

# {}.issubset
# se um conjunto conter outro conjunto dentro

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
conjunto_a.issubset(conjunto_b) #True
conjunto_b.issubset(conjunto_a) #False

# {}.isdisjoint
# utilizado quando um conjunto não faz parte de outro
# verificação para saber se é verdade ou falso

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}


conjunto_a.isdisjoint(conjunto_b) #True
conjunto_b.isdisjoint(conjunto_c) #False


# {}.add
# adiciona um novo item no elemento
sorteio = {1, 23}
sorteio.add(25) # {1, 23, 25}

# {}.clear 
# vai pegar o conjunto e limpar

# {}.copy
# vai copiar o seu conjunto

# {}.discard
# vai descartar um item

# {}.pop
# o metodo pop no set vai tirar o item da frente e não o ultimo item

# {}.remove
# se o elemento não existir no set, ele acusa um erro

# len
# vai achar o tamanho do set

# para verificar se um elemento esta no conjunto
# utilizaremos o in

