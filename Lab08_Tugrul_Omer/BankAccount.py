class BankAccount:
    def __init__(self,account_num,balance=0):
        self.__account_num=account_num
        self.__balance=balance

    def get_account(self):
        return self.__account_num

    def deposit(self,value):
         self.__balance=float(self.__balance)+float(value)

    def withdraw(self,value):
        if float(self.__balance)-float(value)<0:
            print("There is not enough money!")
            print(value,"cannot be withdrawn from account",self.__account_num,"\n")
            return False
        else:
            self.__balance=float(self.__balance) - float(value)
            return True

    def transfer(self,other_acc,val):
        if self.withdraw(val):
            other_acc.deposit(val)

    def __repr__(self):
        return "Account Number: "+str(self.__account_num)+"\n"+"Balance: "+str(self.__balance)+"\n"


class SavingsAccount(BankAccount):
    def __init__(self,account_num,rate,balance):
        super().__init__(account_num,balance)
        self.__rate=rate

    def add_interest(self,value):
        return float(self.__balance)+float(value)*float(self.__balance)/100



