class CategoriasGrupo:
    def __init__(self, categorias):
        self.oficiais = []
        self.nao_oficiais = []
        self.group_categorias(categorias)

    def group_categorias(self, categorias):
        for categoria_info in categorias:
            if categoria_info.oficial:
                self.oficiais.append(categoria_info)
            else:
                self.nao_oficiais.append(categoria_info)