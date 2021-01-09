class User:
    def __init__(self, name, balance):
        self.individualname = name
        self.accountbalance = balance
    
    def subbalance(self, amount):
        self.accountbalance -= amount
        return self
# return self is needed for chaining

    def addbalance(self, amount):
        self.accountbalance += amount
        return self
#  return self is needed for chaining
    
    def displaybalance(self):
        print(f"User:{self.individualname}, Balance: ${self.accountbalance}")

    def transfermoney(self, other_user, amount):
        self.accountbalance -= amount
        other_user.accountbalance += amount

    

#This is creating instances of user class (user objects)
User1 = User("Guido van Rossom", 320.00)
User2 = User("Duke Forsyth", 150.00)
User3 = User("Zaeema Zafar", 100.00)
print(User1.individualname)


User1.subbalance(150.00).addbalance(10.00).addbalance(10.00).addbalance(10.00)
User2.subbalance(10.00).subbalance(10.00).addbalance(20.00).addbalance(10.00)
User3.subbalance(10.00).subbalance(10.00).subbalance(10.00).addbalance(20.00)
# This is adding subtracting and then adding money to Guido's account
# Through chaining

User1.displaybalance()
User2.displaybalance()
User3.displaybalance()

User1.transfermoney(User2, 100.00)




