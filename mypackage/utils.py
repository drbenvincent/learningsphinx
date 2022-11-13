"""Utility functions for my package"""
import pandas as pd


class DataThing:
    """
    This is a special class for holding strange-shaped data
    """

    def __init__(self):
        self.name = None
        self.dataframe = None

    def do_an_operation(self, thingy: bool = False) -> pd.DataFrame:
        """
        This method does an operation on some data

        :param thingy: A flag to do a thing or not do a thing.
        """
        return self.dataframe


def my_utility_function(input_value: float) -> float:
    """
    This is a utility function

    :param input_value: An input value to do stuff with.
    """
    return input_value * 2


# Functions without docstrings are not picked up by autodoc
def an_undocumented_function(x: float) -> float:
    return x * 5
