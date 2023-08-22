class Conta:
    def soma(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        som = num1+num2
        print(num1," + ",num2," = ",som)
        
numeros = Conta()
numeros.soma(10,5)