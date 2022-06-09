class Split:
    def __init__(self, user):
        self._user = user
        self._amount = None

    def get_user(self):
        return self._user

    def set_user(self, user):
        self._user = user

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount
