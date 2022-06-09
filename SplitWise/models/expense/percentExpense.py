from models.expense.expense import Expense


class PercentExpense(Expense):
    def __init__(self, amount, paid_by, splits, metadata):
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self):
        splits = self.get_splits()
        percent_sum = 0
        for split in splits:
            if type(split) != PercentExpense:
                return False

            percent_sum += split.get_percent()

        total_percent = 100
        if percent_sum != total_percent:
            return False

        return True
