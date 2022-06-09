from models.split.split import Split


class PercentSplit(Split):

    def __init__(self, user, percent):
        super().__init__(user)
        self._percent = percent

    def set_percent(self, percent):
        self._percent = percent

    def get_percent(self):
        return self._percent
