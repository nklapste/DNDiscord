"""Class definitions of both player and non-player characters"""

###########################
# Race definitions
###########################


class BaseRace:
    def __init__(self):
        pass

    def get_race_perks(self):
        pass


###########################
# Default race definitions
###########################


###########################
# Custom race definitions
###########################


class CustomRace(BaseRace):
    def __init__(self):
        super().__init__()
        pass

    def get_race_perks(self):
        pass


###########################
# Character class definitions
###########################


class BaseClass:
    def __init__(self):
        pass


class CustomClass(BaseClass):
    def __init__(self):
        super().__init__()
        pass


###########################
# Character definitions
###########################


class BaseCharacter:
    def __init__(self, name: str = None, race: BaseRace=None):
        # basic stats
        self.hitpoints = 10
        self.inventory = {}
        self.abilities = {}

        # unique quality
        self.name = name
        self.race = race
        if self.race is not None:
            self.abilities.update(self.race.get_race_perks())


class NonPlayerCharacter(BaseCharacter):

    def __init__(self, name: str = None, race: BaseRace = None):
        super().__init__(name, race)
        self.ai = None  # TODO


class PlayerCharacter(BaseCharacter):
    def __init__(self, player_id, name: str, race):
        super().__init__(name, race)
        self.owner = player_id

