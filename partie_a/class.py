#Dans ce fichier, les differentes classes sont cree


class Etudiant:
    def __init__(self, nom, note):
        assert type(nom) == str
        assert type(note) == float or type(note) == int
        self.nom = nom
        self.note = note