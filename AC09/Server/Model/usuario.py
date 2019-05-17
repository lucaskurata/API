class Usuario():
    def __init__(self, id_Usuario, nome, segredo):
        self.id_Usuario = id_Usuario
        self.nome = nome
        self.segredo = segredo

    def __dict__(self):
        dicio = dict()
        dicio['id_Usuario'] = self.id_Usuario
        dicio['nome'] = self.nome
        dicio['segredo'] = self.segredo
        return dicio

    @staticmethod
    def cria(dados):
        try:
            id_Usuario = dados["id_Usuario"]
            nome = dados["nome"]
            segredo = dados["segredo"]
            return Usuario(id_Usuario = id_Usuario, nome = nome, segredo = segredo)
        except Exception as e:
            print("Problema ao criar Usuario!")
            print(e)
    
    @staticmethod
    def cria_de_tupla(dados):
        try:
            id_Usuario = dados[0]
            nome = dados[1]
            segredo = dados[2]
            return Usuario(id_Usuario = id_Usuario, nome = nome, segredo = segredo)
        except Exception as e:
            print("Problema ao criar Usuario!")
            print(e)
        