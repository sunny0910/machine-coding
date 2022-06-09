from models.expense.expense import Expense


class ExactExpense(Expense):
    def __init__(self, amount, paid_by, splits, metadata):
        super().__init__(amount, paid_by, splits, metadata)

    def validate(self):
        split_sum = 0
        splits = self.get_splits()
        for split in splits:
            if type(split) != ExactExpense:
                return False

            split_sum += split.get_amount()

        amount = self.get_amount()
        if amount != split_sum:
            return False

        return True
