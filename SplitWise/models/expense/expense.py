class Expense:
    def __init__(self, amount, paid_by, splits, metadata):
        self._id = 0
        self._amount = amount
        self._paid_by = paid_by
        self._splits = splits
        self._metadata = metadata

    def get_id(self):
        return self._id

    def set_id(self, expense_id):
        self._id = expense_id

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_paid_by(self):
        return self._paid_by

    def set_paid_by(self, paid_by):
        self._paid_by = paid_by

    def get_splits(self):
        return self._splits

    def set_splits(self, splits):
        self._splits = splits

    def get_metadata(self):
        return self._metadata

    def set_metadata(self, metadata):
        self._metadata = metadata
