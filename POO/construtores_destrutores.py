# método construtor(inicializador)
# sempre é executado quando uma nova instância da classe é criada
# nesse método inicializamos o estado do nosso objeto
# para declara o método construtor da classe
# criamos um método com o nome de __init__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('inicializando a classe...')
        self.nome=nome
        self.cor=cor
        self.acordado = acordado

# Método destrutor
# esse método sempre é executado quando uma instância(objeto) é destruida
# não são tão usados em Python em referência a C++
# para declara o método destrutor da classe
# criamos um método com o nome de __del__

    def __del__(self):
        print('destruindo a instância')


    def falar(self):
        print('auau')
        
c = Cachorro('fred', 'preto')
c.falar()