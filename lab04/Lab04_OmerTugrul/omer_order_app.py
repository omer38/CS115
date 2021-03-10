from order import find_order,find_order_items

name = input("Enter customer name to search(exit to quit): \n")

while name!='exit':
    count=0
    if find_order('customers.txt',name)==-1:
        print('Customer Not Found')
    else:
        for i in find_order_items('orders.txt',find_order('customers.txt',name)):
            if count==0:
                price=i
            elif count==1:
                orders=i
            count+=1
        if price==0:
            print("Order Not Found!")
        else:
            new_orders=orders.replace(',','\n')
            print("Order Summary:\n"+new_orders+"Total Order Price: "+ str(price))
            file = open(str((find_order('customers.txt',name))+'.txt'),'a')
            file.write(name+'\n'+"Total Order Price: "+ str(price)+'\n')
            file.close()

    name = input("Enter customer name to search(exit to quit): \n")
