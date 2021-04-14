from BankAccount import BankAccount,SavingsAccount

def readCustomers(fn):
    file = open(fn,"r")
    acc_list=[]
    for line in file:
        line=line.strip()
        datas=line.split(",")
        acc_list.append(SavingsAccount(datas[0],float(datas[2]),float(datas[1])))
    file.close()
    return acc_list

def findCustomerIndex(acc_list,acc_num):
    for el in range(len(acc_list)):
        if acc_num==acc_list[el].get_account():
            return el

def makeOperations(fn,acc_list):
    file = open(fn,"r")
    for line in file:
        line=line.strip()
        l=line.split(";")
        if l[1]=="W":
            index=findCustomerIndex(acc_list,l[0])
            acc_list[index].withdraw(float(l[2]))
        elif l[1]=="D":
            index = findCustomerIndex(acc_list, l[0])
            acc_list[index].deposit(float(l[2]))
        elif l[1]=="T":
            index = findCustomerIndex(acc_list, l[0])
            index2= findCustomerIndex(acc_list,l[3])
            acc_list[index].transfer(acc_list[index2],float(l[2]))


sav_acc_list=readCustomers("customer.txt")
makeOperations("account.txt",sav_acc_list)
for obj in sav_acc_list:
    print(obj)

