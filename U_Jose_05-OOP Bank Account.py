#### For this challenge, create a bank account class that has two attributes:
#### owner
#### balance
#### and two methods: deposit and withdraw
#### As an added requirement, withdrawals may not exceed the available balance.
####
#### Instantiate your class, make several deposits and withdrawals,
#### and test to make sure the account can't be overdrawn.


class Account:
    def __init__(self, owner, balance, password=1):
        self.owner = owner
        self.balance = balance
        self.password = password

    def deposit(self):
        dep_amount = int(input('Please, enter the amount of your deposit: '))
        self.balance += dep_amount
        print(f' You have deposited {dep_amount}rub. Your balance is {self.balance}rub.')
        return self.balance

    def withdraw(self):
        dep_amount = int(input('Please, enter the amount of your withdraw: '))
        if (self.balance - dep_amount) < 0:
            print(f' Tne withdrawal exceeds the available balance {self.balance}rub.')
        else:
            self.balance -= dep_amount
            print(f' You have withdrawn {dep_amount}rub. Your balance is {self.balance}rub.')
            return self.balance


    def checking_balance(self):
        if self.balance > 0:
            return True
        else:
            return False

    def continue_(self):
        finish_operations = input(f'{self.owner}, do you wanna continue operations with your account, y or n:')
        if finish_operations == 'y':
            return True
        else:
            return False

    def checking_name_password(self):
        checking = False
        password = 'wrong'
        name = 'wrong'
        while name != acct1.owner and password != acct1.password:
            name = input('Please, enter name: ')
            password = input('Please, enter password: ')
            if name != acct1.owner and password != acct1.password:
                print('name and password are not correct')

        print(f'Hi {name}!')
        print(f'Account balance: {acct1.balance}')
        checking = True
        return checking

    def choose_activity(self):
        choose_operation = 'wrong'
        while choose_operation not in ['D', 'W']:
            choose_operation = input('Would you like to deposit (D) or withdraw (W) money? ').upper()
            if choose_operation not in ['D', 'W']:
                print(f'this operation "{choose_operation}" is not supported')
        return choose_operation


acct1 = Account('i', 100)

print('Welcome to the Bank')


acct1.checking_name_password()
while True:
    owner_choice = acct1.choose_activity()
    if owner_choice == 'D':
        acct1.deposit()
    else:
        acct1.withdraw()

    if not acct1.continue_():
        print('Goodbye!')
        break