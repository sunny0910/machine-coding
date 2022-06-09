from services.expense import Expense


class ExpenseManager:

    def __init__(self):
        self.balance_sheet = {}
        self.user_map = {}
        self.expenses = []

    def add_user(self, user):
        self.user_map[user.get_id()] = user
        self.balance_sheet[user.get_id()] = {}

    def add_expense(self, expense_type, amount, paid_by, splits):
        expense = Expense.create_expense(expense_type, amount, self.user_map[paid_by], splits)
        self.expenses.append(expense)

        splits = expense.get_splits()
        for split in splits:
            paid_to = split.get_user().get_id()
            # balance_sheet = self.balance_sheet[paid_by]
            if paid_to not in self.balance_sheet[paid_by]:
                self.balance_sheet[paid_by][paid_to] = 0.0

            self.balance_sheet[paid_by][paid_to] = self.balance_sheet[paid_by][paid_to] + split.get_amount()

            # balances = self.balance_sheet[paid_to]
            if paid_by not in self.balance_sheet[paid_to]:
                self.balance_sheet[paid_to][paid_by] = 0.0
            self.balance_sheet[paid_to][paid_by] = self.balance_sheet[paid_to][paid_by] - split.get_amount()
            # self.balance_sheet[paid_to] = balances[paid_by]

    def show_user_balance(self, user_id):
        is_empty = True
        users_balance_sheet = self.balance_sheet.get(user_id)
        for user2_id, user_balance in users_balance_sheet.items():
            if user_balance != 0:
                is_empty = False
                self.print_balance(user_id, user2_id, user_balance)

        if is_empty:
            print("No balances")

    def show_balance(self):
        is_empty = True
        for user, balances in self.balance_sheet.items():
            for user2, amount in balances.items():
                if amount > 0:
                    is_empty = False
                    self.print_balance(user, user2, amount)

        if is_empty:
            print("No balances")

    def print_balance(self, user1, user2, amount):
        user1_name = self.user_map[user1].get_name()
        user2_name = self.user_map[user2].get_name()

        if amount < 0:
            print('%s has to pay %s - %d' % (user1_name, user2_name, -amount))
        else:
            print('%s owes %s - %d' % (user2_name, user1_name, amount))
