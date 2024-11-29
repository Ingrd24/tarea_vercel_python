class Ejemplo():
 
    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"
 
    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        return "Soy un metodo privado, para ti no existo"
    
    def get_oculto(self):
        return self.__oculto

class Ejemplo():
 
    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"
 
    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        return "Soy un metodo privado, para ti no existo"
    def get_oculto(self):
        return self.__oculto
 
objeto = Ejemplo()
 
print(objeto.publico())
 
print(objeto._Ejemplo__privado())

print(objeto.get_oculto())