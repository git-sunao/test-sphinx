class dog_class:
    def __init__(self, name='wanwan'):
        """
        init function of dog class

        Parameters
        ----------
        name : str, optional
            name of dog, by default 'wanwan'
        """
        self.name = name

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