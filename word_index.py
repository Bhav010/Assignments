
'''
myfile = open('book of John text.txt', 'r')
read1 = myfile.read()

word = 'God'
ctr = 0
for r in read1:
    if r.find(word) == True:
        ctr += 1
print(f" {word} : {ctr}")

#2
word = "life"
ctr = 0
with open (r'book of John text.txt', 'r') as myfile:
    content = myfile.read()
    for i in content:
        if str(word) in content:
            ctr = ctr+1
    print(ctr)    
'''
'''
#3 Working Code!!
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

#4
mydict = {'Father':0, 'God':0, 'Christ':0, 'Spirit':0, 'life':0, 'man':0}
with open ('book of John text.txt', 'r') as myfile:
    for line in myfile:
        words = line.split()        #splits text/string into a list
        for i in words:
            if i in mydict:
                mydict[i] += 1
                
for key, value in mydict.items():
    print(key, ":", mydict[key])
