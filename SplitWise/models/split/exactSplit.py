from models.split.split import Split


class ExactSplit(Split):

    def __init__(self, user, amount):
        super().__init__(user)
        self._amount = amount
