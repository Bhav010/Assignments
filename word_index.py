

'''
#1 Working Code using list
word = ["life", "God"]
ctr = [0,0]
#ctr1 = 0
with open ('book of John text.txt', 'r') as myfile:
    for line in myfile:
        words = line.split()        #splits text/string into a list
        for i in words:
            if (i==word[0]):
                ctr[0] = ctr[0]+1
            if (i==word[1]):
                ctr[1] = ctr[1]+1
                
print(f"{word[0]}: {ctr[0]}")  
print(f"{word[1]}: {ctr[1]}")  
'''

#2 Using dictionary
mydict = {'Father':0, 'God':0, 'Christ':0, 'Spirit':0, 'life':0, 'man':0}
j={}
with open ('book of John text.txt', 'r') as myfile:
    for line in myfile:
        words = line.split()        #splits text/string into a list
        for i in words:
            if i in mydict:
                mydict[i] += 1
                if i!= i.title():
                    #print('Case different')
                    #mydict[i]=i.title()
                    #for i,[i] in mydict:
                    mydict[i.title()].append(mydict[i]+1)
                    #mydict[j] +=1
                
for key, value in mydict.items():
    print(key, ":", mydict[key])

'''

s = 'hello'
print(s.title())            #capitalizes first letter
'''