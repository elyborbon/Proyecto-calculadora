class Calculadora:
    def __init__(self, numero1,numero2):
        self.numero1 = numero1 
        self.numero2 = numero2

    def suma (self):
        sumaT= self.numero1 + self.numero2
        print (sumaT)

    def resta (self):
        restaT= self.numero1 - self.numero2
        print (restaT)

    def multiplicacion (self):
        multiplicacionT= self.numero1 * self.numero2
        print (multiplicacionT)
    def division (self):
        divisionT= self.numero1 / self.numero2
        print (divisionT)

    def info(self):
        print ("Que operacion quieres ")
        operacion = int(input("Coloca el valor: "))
        if operacion ==1:
            Calculadora.suma(self)
            print ("Pulsa 5 para elegir otra operacion: ")
            numero_2 = int (input("Elige la opcion: "))
            if numero_2 == 5:
                Calculadora.info (self)
        elif operacion == 2: 
            Calculadora.resta(self)
            print ("Pulsa 5 para elegir otra operacion: ")
            numero_2 = int (input("Elige la opcion: "))
            if numero_2 == 5:
                Calculadora.info (self)
        elif operacion == 3: 
            Calculadora.multiplicacion(self)
            print ("Pulsa 5 para elegir otra operacion: ")
            numero_2 = int (input("Elige la opcion: "))
            if numero_2 == 5:
                Calculadora.info (self)
        else:
            Calculadora.division(self)
            numero_2 = int (input("Elige la opcion: "))
            print ("Pulsa 5 para elegir otra operacion: ")
            if numero_2 == 5:
                Calculadora.info (self)
        

Operacion1 = Calculadora(2,5)
Operacion1.info()