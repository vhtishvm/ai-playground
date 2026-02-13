#This is our raw data
a = "Hello my name is Ahtisham ali"

#Converting this raw data into a list of words
b = a.split()
print(b)


#Assigning a unique key to each word in the list
c = {}
counter_id = 0

for item in b:
    if item not in c:
        c[counter_id] = item
        counter_id +=1

print(c)

tokens = []

for x in b:
    tokens.append(x)
    