def main():
    x = int (input ("What's x? " ))
    print ("x squared is ", square(x))


def square(n):
    return n * n

if __name__ == "__main__":
    main()


'''
#API Requests
import requests
import sys
import json

if len (sys.argv) !=2: 
    sys.exit()

response = requests.get ("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
i = 0

for result in o["results"]:
    i += 1
    print (i)
    print (result["trackName"])



import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.kitty("Hello, " + sys.argv[1])
    cowsay.cow("Hello, " + sys.argv[1])
    cowsay.meow("Hello, " + sys.argv[1])
    cowsay.miki("Hello, " + sys.argv[1])
    cowsay.ghostbusters("Hello, " + sys.argv[1])
    cowsay.daemon("Hello, " + sys.argv[1])




# or cowsay.think()


#Slices

import sys

if len(sys.argv) < 2:
    sys.exit ("Too few arguments")

for arg in sys.argv[:-1]:
    print ("hello, my name is ", arg)




#System Functions
#sys.argv (argument vector)

import sys

if len(sys.argv) < 2:
    print ("too few args")
elif len (sys.argv) > 2:
    print ("too many args")
else:
    print ("hello, my name is", sys.argv[1])
#try: 

#except IndexError:
#   print ("Too few Argument, pass at least one ")

#Statistics 
import statistics

print (statistics.mean ([100, 90]))



#Shuffle program
import random

cards = ["jack", "quen", "king"]

random.shuffle (cards)
for card in cards: 
    print (card)



def main(): 
    x = get_int()
    print (f"x is {x}")

def get_int():
    while  True:
        try:
            x = int (input ("What's x ? " ))
        except ValueError:
            print ("x is not an integer")
        else:
            return x

main()






#takes the values on the run-time and gives the output
import sys
print (sys.argv)

total = int(sys.argv[1]) + int (sys.argv[2])
print(f'sum is {total}')



def main():
    print_column(3)

def print_column(height):
    print ("#\n" * height, end="")

main()




astudents = ["Hello", "Harry", "Ron", "Draco"]
ahouses = ["house1", "house-2", "House-3", "House-4"]

students = {"Harry": "house-1", 
    "Honey": "House-2", 
    "Sami": "house-3"}


for student in students:
    print (student, students[student], sep= ", ")



#Loop
students = ["sultan", "rabail", "anusha"]

for i in range (len(students)):
    print (i+1, students[i])

#for _ in students:
#    print (_)


def main():
    meow(3)

def meow (n):
    for _ in range (n):
        print ("meow")

main()


while True:
    n = int(input ("What's n ? "))
    if n > 0:
        break

for _ in range(n):
    print ("Hello")


i = [0,1,2,3]
#x = 0
for x in range(1000):
    print (x)


i = 0
x = 0
while i < 5 :
    print ("meow")
    i = i + 1
    print (i)
    if i == 3:
        break
    


i = 50

x = 0

#for x in range(i):
    print ('Iteration no:',x + 1)
    print (f'Meow {x+1}')
'''   
    
