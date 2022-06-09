from services.expenseManager import ExpenseManager
from models.user import User
from models.split.splitType import SplitType
from models.split.equalSplit import EqualSplit
from models.split.exactSplit import ExactSplit
from models.split.percentSplit import PercentSplit


class Driver:
    @staticmethod
    def main():
        expense_manager = ExpenseManager()
        user1 = User('u1', 'sunny R', 'sunny@gmail.com', '1234')
        user2 = User('u2', 'john doe', 'john.doe@gmail.com', '1234')
        user3 = User('u3', 'lorem ipsum', 'lorem.ipsum@gmail.com', '1234')

        expense_manager.add_user(user1)
        expense_manager.add_user(user2)
        expense_manager.add_user(user3)

        while True:
            print("Enter command")
            command = input()
            commands = command.split(" ")
            command_type = commands[0]

            if command_type == "SHOW":
                if len(commands) == 1:
                    expense_manager.show_balance()
                else:
                    expense_manager.show_user_balance(commands[1])
            elif command_type == "EXPENSE":
                paid_by = commands[1]
                amount = float(commands[2])
                number_of_users = int(commands[3])
                expense_type = commands[4+number_of_users]
                splits = []
                if expense_type == SplitType.EQUAL.value:
                    for i in range(number_of_users):
                        split = EqualSplit(expense_manager.user_map[commands[4+i]])
                        splits.append(split)
                
                    expense_manager.add_expense(SplitType.EQUAL.value, amount, paid_by, splits)

                elif expense_type == SplitType.EXACT.value:
                    for i in range(number_of_users):
                        split = ExactSplit(expense_manager.user_map[commands[4+i]], float(commands[5 + number_of_users + i]))
                        splits.append(split)
                        
                    expense_manager.add_expense(SplitType.EXACT.value, amount, paid_by, splits)
                    
                elif expense_type == SplitType.PERCENT.value:
                    for i in range(number_of_users):
                        split = PercentSplit(expense_manager.user_map[commands[4+i]], float(commands[5 + number_of_users + i]))
                        splits.append(split)
                    
                    expense_manager.add_expense(SplitType.PERCENT.value, amount, paid_by, splits)
                else:
                    raise Exception()


if __name__ == '__main__':
    Driver.main()
