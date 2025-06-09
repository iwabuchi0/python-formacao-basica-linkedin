class Gata:
    def __init__(self, nome='Nísia'):
        self.patas = 4
        self.cor = 'preta'
        self.nome = nome
    
    def som(self):
        print(self.nome + ' é uma gata que mia')

minha_gata = Gata()
gata_vizinha = Gata()
gata_bairro = Gata('Sara')

gata_bairro.som()