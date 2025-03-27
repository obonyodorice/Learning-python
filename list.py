fruits=['Banana','Orange','Apple','Mango','Kiwi']
# newlist=[x.upper() for x in fruits if x != 'Orange']
# newlist=[]

# newlist.append(fruits)

# print(newlist)           
for i in range(len(fruits)):
    print(f'{i}.{fruits[i]}')