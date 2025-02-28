class CuentaBancaria:
    __saldo = 0
    def __init__(self,nombre="indefinido"):
        self.__nombre = nombre
    @property 
    def saldo(self):
        return self.__saldo
    @saldo.setter 
    def saldo(self,saldo):
        self.__saldo = saldo
    @property 
    def nombre(self):
        return self.__nombre
    
    def depositar(self,deposito=0):
        if deposito <= 0:
            print('Error')
        else:
            self.saldo = self.saldo + deposito
        print('Deposito con exito')
    
    def retirar(self,retiro=0):
        if retiro > 0:
            if retiro <= self.saldo:
                self.saldo = self.saldo - retiro
                print('Retiro con exito')
            else: 
                print('Saldo insuficiente')
        else:
            print('Error')
    
    def mostrar_saldo(self):
        print(f'Nombre: {self.nombre}\nSaldo: {self.saldo}')

def menu():
    nombre = input('Nombre: ')
    titular = CuentaBancaria(nombre)
    
    while(True):
        op = int(input((f'1) Depositar\n2) retirar\n3) mostrar saldo\n4) Salir\nop: ')))
        if op == 1:
            deposito = int(input('Deposito: '))
            titular.depositar(deposito)
        elif op == 2:
            retirar = int(input('Retiro: '))
            titular.retirar(retirar)
        elif op == 3:
            titular.mostrar_saldo()
        elif op == 4:
            break
        else:
            print('Opcion no valida')   
        input('Enter para continuar...')     
menu()