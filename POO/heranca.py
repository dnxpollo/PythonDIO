# Herança

# capacidade de uma classe filha derivar ou herdar as características
# e comportamentos da classe mãe(base)
# representa bem os relacionamentos do mundo real
# fornece reutilização de código
# é de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A

# class A:
#     pass 

# class A(B):
#     pass

# Herança simples e Herança múltipla
# Herança simples

# class Veiculo:
#     def __init__(self, cor, placa, numero_rodas):
#         self.cor = cor
#         self.placa = placa
#         self.numero_rodas = numero_rodas
    
#     def ligar_motor(self):
#         print('ligando o motor')

# class Motocicleta(Veiculo):
#     pass

# class Carro(Veiculo):
#     pass

# class Caminhao(Veiculo):
#     def __init__(self, cor, placa, numero_rodas, carregado):
#         super().__init__(cor, placa, numero_rodas)
#         self.carregado = carregado

#     def esta_carregado(self):
#         print(f"{'Sim' if self.carregado else 'Não'} estou carregado")







# moto = Motocicleta('preta', 'abc-1234', 2)
# moto.ligar_motor()

# carro = Carro('branco', 'xde-9876', 4)
# carro.ligar_motor()

# caminhao = Caminhao('cinza', 'nde-7490', 8, False)
# caminhao.ligar_motor()
# caminhao.esta_carregado()
# print(carro)
# print(moto)


# Herança Múltipla
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, nro_patas, cor_pelo):
        self.cor_pelo = cor_pelo
        super().__init__(nro_patas)

class Ave(Animal):
    def __init__(self, nro_patas, cor_bico):
        super().__init__(nro_patas)

class Cachorro(Mamifero):
    def __init__(self, nro_patas):
        super().__init__(nro_patas)


class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(4, 'preto e branco')
print(gato)

ornitorrinco = Ornitorrinco(4, 'marrom')
print(ornitorrinco)