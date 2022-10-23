# write dict to have switch name / model / pod

def l():
    return ("\n")

print (l())

dc1 = [{"name": "Border", "model": "N9k-1", "pod": "101"}, 
{"name": "Services", "model": "N9k-2", "pod": "102"}, 
{"name": "Compute", "model": "N9k-3", "pod": "103"}
]
i = len(dc1)

print (i)

for i in dc1:
    if i != len(dc1):
        #print (i, "The value of i is", len(dc1))
        print (i ["name"], i ["model"], i ["pod"], sep = ", ")
        i =- 1
    else:
        print (f'didnt find anything and value of i is {i}')

#print (dc1[0], l(), dc1[1], l(),dc1[2], sep = l()

'''
for dc2 in dc1:
    print (dc2, dc1[dc2], sep= ": ")
'''