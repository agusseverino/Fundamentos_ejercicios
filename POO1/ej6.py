class calculadora():
    def cargar(self, numero):
        self.inicial = numero

    def sumar(self, numero):
        self.inicial += numero
    
    def restar(self, numero):
        self.inicial -= numero

    def multiplicar(self, numero):
        self.inicial *= numero

    def dividir(self, numero):
        self.inicial /= numero

    def ValorActual(self):
        print(self.inicial)

calculadora = calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.ValorActual()