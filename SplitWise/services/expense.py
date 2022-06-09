from models.expense.equalExpense import EqualExpense
from models.expense.percentExpense import PercentExpense
from models.expense.exactExpense import ExactExpense
from models.split.splitType import SplitType


class Expense:

    @staticmethod
    def create_expense(expense_type, amount, paid_by, splits):
        if expense_type == SplitType.EQUAL.value:
            total_splits = len(splits)
            split_amount = amount/total_splits

            for split in splits:
                split.set_amount(split_amount)

            splits[0].set_amount(split_amount + (amount - split_amount*total_splits))

            return EqualExpense(amount, paid_by, splits, None)
        elif expense_type == SplitType.PERCENT.value:
            for split in splits:
                split.set_amount((amount * split.get_percent())/100.0)

            return PercentExpense(amount, paid_by, splits, None)
        elif expense_type == SplitType.EXACT.value:
            return ExactExpense(amount, paid_by, splits, None)
        else:
            raise Exception()
