# conjunto não ordenado de par chave:valor
# para ser chave precisa ser imutável(tupla)
# o valor pode ser mutável(lista)
# são delimitados por {}
# palavra reservada é dict

pessoa = {'nome':'Sérgio', 'idade': 28}
pessoa = dict(nome='Sérgio', idade=28)
pessoa['telefone'] = '3333-1234'

# Dicionarios aninhados
# armazenam qualquer valor desde que a chave seja um objeto imutável

# podemos iterar o dicionário, e a forma mais comum é com o for

# metodos

# clear
# apaga todos os dados do dicionario
contatos = {
    'sergio@gmail.com': {'nome': 'Sérgio', 'telefone': '3333-2222'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': '3333-2223'},
    'rafaelle@gmail.com': {'nome': 'Rafaelle', 'telefone': '3333-2224'},
    'tarzan@gmail.com': {'nome': 'Tarzan', 'telefone': '3333-2225'}
}

contatos.clear()


# copy 
# similar aos demais copy
# faz uma cópia do dicionário criando um novo dicionário a partir de outro

mercado = {
    'lista': {'fruta': 'banana', 'legume':'batata'}
}

copia_mercado = mercado.copy()
copia_mercado = {'fruta': 'laranja'}
print(mercado, copia_mercado)

# fromkeys 
# pode ser usado para inicializar várias chaves com o mesmo valor
# pode criar rápidamente um dicionário com várias chaves

dict.fromkeys(['nome', 'telefone']) # retorna None
dict.fromkeys(['nome', 'telefone'], 'vazio') # atribui um valor a chave nome

# {}.get
# tenta acessar o valor de uma chave
# se a chave existe, retorna o valor
# se a chave não existe, por padrão pode ser None
# mas pode ser configurado um default

contatos = {
    'sergio@gmail.com':{'nome': 'Sérgio', 'telefone': '3333-2221'}
}

print(contatos['chave']) #vai gerar um KeyError pois essa chave não existe
contatos.get('chave') # gera None pois a chave não existe mas o metodo get não deixa gerar um erro
contatos.get('chave', {}) # gera uma lista vazia
contatos.get('sergio@gmail.com', {}) # vai buscar o valor do dicionário


# {}.items
# retorna uma lista de tuplas

contatos = {
    'sergio@gmail.com':{'nome': 'Sérgio', 'telefone': '3333-2221'}
}

contatos.items() #dict_items([('sergio@gmail.com', {'nome': 'Sérgio', 'telefone': '3333-2221'})])


# {}.keys
# util quando quer saber
# as chaves que o seu dicionário tem
# vai retornar um objeto chamado dict_keys
# não copia a chave só oferece uma referência dinâmica
# se o dicionário mudar, o objeto dict_keys refelte


novo_dicionario = {'a': 100, 2: 'teste', 'b': 'python'}
print(novo_dicionario.keys())



# {}.pop
# remove e retorna o valor da chave removeu
# pode ser configurado um default
# caso a chave não exista no dicionário

novo_dicionario = {'a': 100, 2: 'teste', 'b': 'python'}
print(novo_dicionario.pop('nome', {'teste':'outro'}))

# .{}popitem
# não informa a chave
# retira na sequência
# gera um KeyError se estiver vazia
# retira o ultimo valor inserido 

contatos = {
    'sergio@gmail.com':{'nome': 'Sérgio', 'telefone': '3333-2221'},
    'apolllo@gmail.com':{'nome': 'Apollo', 'telefone': '3333-2222'}
}
print(contatos.popitem())
print(contatos)

# {}.setdefault
# usado para criar um valor
# para chaves que não existem
# se a chave já existe, retorna o valor dela
# se a chave não existe, cria essa chave no dicionário 
# com o valor fornecido e retorna esse valor.

contato = {'nome': 'sergio', 'telefone': '2222-2221'}
contato.setdefault('nome', 'apollo') # não vai retornar apollo pois já existe um valor para essa chave
contato.setdefault('idade', 28)
print(contato)


# {}.update
# atualiza um dicionário com pares chave-valor 
# vindos de outro dicionário ou objeto iterável

contato = {'nome': 'sergio', 'telefone': '2222-2221'}
contato.update('nome', 'apollo') # vai retornar apollo pois o valor da chave nome foi atualizado


# {}.values 
# retorna os valores de todas as chaves

contatos = {
    'sergio@gmail.com': {'nome': 'Sérgio', 'telefone': '3333-2222'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': '3333-2223'},
    'rafaelle@gmail.com': {'nome': 'Rafaelle', 'telefone': '3333-2224'},
    'tarzan@gmail.com': {'nome': 'Tarzan', 'telefone': '3333-2225'}
}

contatos.values()
print(contatos)

# in 
# verifica se uma chave existe no dicionario

contatos = {
    'sergio@gmail.com': {'nome': 'Sérgio', 'telefone': '3333-2222'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': '3333-2223'},
    'rafaelle@gmail.com': {'nome': 'Rafaelle', 'telefone': '3333-2224'},
    'tarzan@gmail.com': {'nome': 'Tarzan', 'telefone': '3333-2225'}
}

'sergio@gmail.com' in contatos # True
'idade' in contatos # False

# del
# faz exclusão de chaves

contatos = {
    'sergio@gmail.com': {'nome': 'Sérgio', 'telefone': '3333-2222'},
    'apollo@gmail.com': {'nome': 'Apollo', 'telefone': '3333-2223'},
    'rafaelle@gmail.com': {'nome': 'Rafaelle', 'telefone': '3333-2224'},
    'tarzan@gmail.com': {'nome': 'Tarzan', 'telefone': '3333-2225'}
}

del contatos['sergio@gmail.com']['telefone']
print(contatos)
