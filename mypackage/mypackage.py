class Grapes:

    """
    This is a class for grapes
    """

    def __init__(self):
        self.name = None
        self.rating = None
        self.info = dict()

    def eat_grapes(self):
        """
        Shows the Pokémon name and its evolution.
        """
        print(f"I am eating some grapes.")


class WhiteGrapes(Grapes):
    """
    Whitegrapes information here
    Along with :class:`RedGrapes`, these are all grapes.
    """

    def __init__(self):
        self.name = "WhiteGrapes"


class RedGrapes(Grapes):
    """
    RedGrapes information here.
    Along with :class:`WhiteGrapes`, these are all grapes.
    """

    def __init__(self):
        self.name = "RedGrapes"
