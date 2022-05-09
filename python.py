
class User:
    def __init__(self,name,email):
        self.name = name
        self.email= email
        self.account_balance=0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self  #because we return self we can do something called chaining 
    def _user_balance(self):
        print(f"User:{self.name}, Balance:{self.account_balance}")
    def transfer_money(self,amount,ouser):
        self.account_balance -= amount
        ouser.account_balance += amount
        self._user_balance()
        ouser._user_balance()


mondo = User("mondo", "mondo@flhs.org")
# mondo.name = "mondo"
# mondo.email = "mondo@flhs.org"
mondo.make_deposit(100).make_deposit(100).make_deposit(100).make_deposit(200) #chaining
mondo._user_balance()

vanessa = User("Vanessa","vannessa0sca@email.com")
vanessa.make_deposit(600)
vanessa._user_balance()

john = User("Johnathan", "johnsbikeshop@email.com")
john.make_deposit(1)
john._user_balance()

mondo.transfer_money(100,vanessa)
mondo._user_balance()