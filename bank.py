import re
import json
records = []
values = []
total = 0 
count = 0 
input_string = ""

with open("bank.csv") as file:
    for line in file:
        date, info, credit, balance, dummy  = line.rstrip().split(',')
        records.append(info)
        values.append (balance)
        #if re.findall(info, "+Matloob-BAF+"):
            #if re.search(r"^[^@]+@[^@]+\.edu$", email):
        #    count = count+1
        #else:
            #print (date, " " , info, "with balance ", balance, "Credit: ", credit, "Dummy: ", dummy)
        #    count = count+1
            
        #print (line.rstrip())
x = ''
y = ''
for y in values:
  print (y)


print (f'Total records: {count}')
#print (type(info), type(credit), type(balance))
#print (f'Total: {total}')


'''
            while debit !='':
                debit = int(debit)
                total = total + int(debit)
                '''