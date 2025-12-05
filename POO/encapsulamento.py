class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
    

conta = Conta('00001', 200)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())

# Recursos públicos e privados
# recurso público só pode ser acessado de fora da classe
# recurso privado só pode ser acessado pela classe
# convenção usada para representar um recurso privado
# Python diferente de C++ e Java, 
# não possui palavras reservadas para representar recursos privados
# o que vai definir se o recurso é privado é a presença do underline no inicio da palavra

print('-----------------------')
print('Inicio do exemplo Foo')


class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0

foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)

print('-----------------')
print('exemplo pesssoa')

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self.ano_nascimento
    
pessoa = Pessoa('Sérgio', 1997)
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade}')