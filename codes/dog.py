#import numpy as np
class dog_class:
    """
    This is dog class

    Attributes
    ----------
    name : str
        name of dog
    belongings : list
        list of belongings

    """
    def __init__(self, name='wanwan'):
        """
        init function of dog class

        Parameters
        ----------
        name : str, optional
            name of dog, by default 'wanwan'

        """
        self.name = name
        self.belongings = []

    def print_name(self):
        """
        printing name of dog

        """
        print(self.name)

    def get_name(self):
        """
        get name of dog

        Returns
        -------
        name : str
            name of dog

        """
        return self.name

    def give_present(self, present):
        """
        give present to dog

        Parameters
        ----------
        present : obj
            anything to give to dog
        """
        self.belongings.append(present)