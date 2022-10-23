#names = []

with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print (line.rstrip())



'''
file = open("names.txt", "a")
while n != 'stop':
    n = input(f"{n}\n")
    file.write(n)
    if n == 'stop':
        break
    
file.close()


###########
with open("names.txt", "r") as file: #to auto close the file
    lines = file.readlines()

for _ in lines:
    print("Hello", _.rstrip())
    ############

#####more better####
with open("names.txt", "r") as file: #to auto close the file
    for line in file:
        print ("Hello, ", line.rstrip())


'''
