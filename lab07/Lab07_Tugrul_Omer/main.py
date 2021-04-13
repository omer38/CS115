from Nation import *

def read_file(fn):
    file=open(fn,'r')
    d={}
    for line in file:
        line=line.strip()
        l=line.split(',')
        d[l[0]]=Nation(l[0],l[1],float(l[2]),float(l[3]))
    file.close()
    return d

country_dic=read_file("country.txt")

c_name=input("Enter a country: ")
print(str(country_dic[c_name]))
con_name=input("Enter a continent: ")

selected=[]

for data in country_dic:
    if con_name==country_dic[data].get_continent():
        selected.append(country_dic[data])

print(sorted(selected))







