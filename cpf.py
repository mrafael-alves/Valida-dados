class Cpf:
    def __init__(self, doc):
        doc = str(doc)
        if self.tamanho_doc(doc):
            self.doc = doc
        else:
            raise ValueError("CPF é inválido!")

    def tamanho_doc(self, doc):
        if len(doc) == 11:
            return True
        else:
            return False