class Coche:
    __combustible = 100
    def __init__(self,marca="indefinido",modelo="indefinido"):
        self.__marca = marca
        self.__modelo = modelo
    @property
    def combustible(self):
        return self.__combustible
    @combustible.setter 
    def combustible(self,combustible):
        self.__combustible = combustible
    @property
    def marca(self):
        return self.__marca
    @marca.setter 
    def marca(self,marca):
        self.__marca = marca
    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter 
    def modelo(self,modelo):
        self.__modelo = modelo
    
    def conducir(self,km):
        recorrido = km/10
        self.combustible = self.combustible - recorrido
        
    def reposar(self,litros):
        if litros < 0:
            return print('Error')
        else: 
            aumentar = self.combustible + litros
            if aumentar >= 100:
                self.combustible = 100
            else:
                self.combustible = aumentar 
        
    def estado(self):
        print(f'{self.marca}\nCombustible: {self.combustible}')

def menu():
    marca = input('Marca del coche: ')
    modelo = input('Modelo del coche: ')
    
    conductor = Coche(marca,modelo)
    
    while(True):
        op = int(input((f'1) Conducir\n2) Repostar\n3) Estado\n4) Salir\nop: ')))
        if op == 1:
            km = int(input('km: '))
            conductor.conducir(km)
        elif op == 2:
            litros = int(input('litros: '))
            conductor.reposar(litros)
        elif op == 3:
            conductor.estado()
        elif op == 4:
            break
        else:
            print('Opcion no valida')   
        input('Enter para continuar...')     
menu()