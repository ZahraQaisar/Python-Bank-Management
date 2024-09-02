import random, string, time

# # Pattern
# # ids = {'customer1':
# #             {'name': 'xyz',
# #              'acc_num': 'FGHJY79876',
# #              'balance': 2345},
# #        'customer2':
# #             {'name': 'xyz',
# #              'acc_num': 'FGHJY79876',
# #              'balance': 2345}
# #        }

ids = []
class Bank:
    bal = 0
    def __init__(self):
        self.id_ = 0
        self.i = 1
        self.user_ids = {}
    
    def unique_id(self, name):
        self.user_name = name
        i = 1
        self.timestamp = str(int(time.time()))
        self.comb_char_dig = string.ascii_uppercase + string.digits # randomly combines U.C letters and digits(0-9)
        self.random_chars = ''.join(random.choices(self.comb_char_dig, k=6)) # combines 6 randoms char mein comb_char_dig
        self.id = f"ID{self.timestamp}{self.random_chars}"
        self.id_ = self.id
        cust = f'customer{self.i}'
        self.i += 1
        
        self.user_ids.update({cust:{self.user_name : self.id, 'Balance': Bank.bal}})
        ids.append(self.user_ids)
        # self.user_ids[self.id] = {'name': self.user_name, 'Balance': 0}
        
    def new_account(self):
        self.name = (input("Enter your full name: ")).lower()    
        self.unique_id(self.name)
        print("New account created!")
        print("Your Account Number is", self.id_)
    
    def deposit(self, acc_list):
        acc_num = input("Enter your account number: ").strip()
        for x in acc_list:
            for customer_key, customer_value in x.items():
                for user_name, user_id in customer_value.items():
                    if user_id == acc_num:
                        amount_to_deposit = int(input("Enter amount you want to deposit: "))
                        # self.user_ids[acc_num]['Balance'] += amount_to_deposit
                        customer_value['Balance'] += amount_to_deposit
                        return 'Amount Deposited'
        return f"{acc_num}, not found!"
    
    def withdraw(self, acc_list):
        acc_num = input("Enter your account number: ").strip()
        for x in acc_list:
            for customer_key, customer_value in x.items():
                for user_name, user_id in customer_value.items():
                    if user_id == acc_num:
                        amount_to_withdraw = int(input("Enter amount to withdraw:"))
                        if customer_value['Balance'] >= amount_to_withdraw:
                            customer_value['Balance'] -= amount_to_withdraw
                            return 'Amount Withdrawed'
                        else:
                            return 'Insufficient balance!'
        return f"{acc_num}, not found!"
    
    def check_balance(self, acc_list):
        acc_num = input("Enter your account number: ").strip()
        for x in acc_list:
            for customer_key, customer_value in x.items():
                for user_name, user_id in customer_value.items():
                    if user_id == acc_num:
                        bal =  customer_value['Balance']
                        return f"Balance for ID {acc_num}: {bal}"
        return f"{acc_num}, not found"
    
    def choice(self):
        choice = input('''Do want to 
                           => deposit money? Enter D 
                           => withdraw money? Enter W
                           => check balance? Enter C
                           => create new account? Enter A
                           => Enter Q to Quit
                           Enter:''').lower()    
        if choice == 'd':
            print(self.deposit(ids))
        elif choice == 'w':
            print(self.withdraw(ids))
        elif choice == 'c':
            print(self.check_balance(ids))
        elif choice == 'a':
            self.new_account()
        elif choice == 'q':
            quit()
        else:
            print("Invalid choice!")

cont = True
user_choice = (input("Do you want to proceed? (Y/N):")).lower()
while(cont):    
    if user_choice == 'y':
        user_input = (input("Do you have an account? (Y/N):")).lower()
        b = Bank()
        if user_input == 'n':
            b.new_account()
            b.choice()
        elif user_input == 'y':
            # print("account already.")
            b.choice()
        else:
            print("Invalid Input!")
    elif user_choice == 'n':
        cont = False
    else:
        print("Invalid Input!")
        
        