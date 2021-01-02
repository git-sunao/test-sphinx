class cat_class:
    def __init__(self, name='nyanya'):
        """
        init function of cat class

        Parameters
        ----------
        name : str, optional
            name of cat, by default 'nyanya'
        """
        self.name = name

    def print_name(self):
        """
        printing name of cat
        """
        print(self.name)

    def get_name(self):
        """
        get name of cat

        Returns
        -------
        name : str
            name of cat
        """
        return self.name