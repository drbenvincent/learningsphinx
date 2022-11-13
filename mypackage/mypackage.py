from typing import Optional


class Grapes:
    """
    This is a class for grapes

    .. math::

       (a + b)^2  =  (a + b)(a + b)

    """

    def __init__(self):
        self.name = None
        self.rating = None
        self.info = dict()

    def eat_grapes(self, n_grapes: Optional[int] = 1) -> None:
        """
        This method leads to eating grapes, :math:`a^2 + b^2 = c^2`.

        :param n_grapes: The number of grapes we'd like to eat.
        """
        print(f"I am eating {n_grapes} grapes.")


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
