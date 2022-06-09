from models.expense.expense import Expense


class EqualExpense(Expense):
    def __init__(self, amount, paid_by, splits, metadata):
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self):
        splits = self.get_splits()
        for split in splits:
            if type(split) != EqualExpense:
                return False

        return True
