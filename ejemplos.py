class Cachorro:
    def __init__(self, color, raza, id):
        self.color = color
        self.raza = raza
        self.id = id

    def __str__(self):
        return """\
        Raza: {}
        Color: {}""".format(self.raza, self.color)
    def __repr__(self) -> str:
        return "<Cachorro {}>".format(self.id)

perrito = Cachorro("Marrón claro", "Golden retriever", 1)

print("Este es un cachorro de la raza {} y es de color {}".format(perrito.raza, perrito.color))

print(repr(perrito))