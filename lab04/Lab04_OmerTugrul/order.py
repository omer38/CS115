
def find_order(file_name,c_name):

    file = open(file_name,'r')
    for line in file:
        name = line.lower()
        pos=name.find(',')
        id=line[0:pos]
        if c_name.lower() == name[pos+1:].strip():
            return id

    return -1
    file.close()


def find_order_items(file_name,c_id):
    new_file=open(file_name,'r')
    total_price=0
    string=""
    for line in new_file:
        pos1 = line.find(";")
        pos2 = line.find(";", pos1 + 1)
        if c_id in line:
            string+=line[pos1+1:pos2]+","
            price = float(line[pos2+1:].strip())
            total_price+=price

    return total_price,string
    new_file.close()







