class Family:
    def __init__(self, name, sigil):
        self.name = name
        self.sigil = sigil

    def get_aggressive(self):
        pass

class Character(Family):

    def __init__(self, family_name, sigil, name, gender):
        self.name = name
        self.gender = gender
        super().__init__(name=family_name, sigil=sigil)
