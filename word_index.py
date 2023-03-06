#1 Using dictionary

#define mydict with given words
mydict = {'Father':0, 'God':0, 'Christ':0, 'Spirit':0, 'spirit':0, 'life':0, 'man':0}  

#read through the file
with open ('book of John text.txt', 'r') as myfile:
    for line in myfile:
        words = line.split()        #splits text/string into a list
        for i in words:             #loop through the list
            if i in mydict:         #loop through the dictionary
                mydict[i] += 1      #increment the value of key in dictionary
                                   
                
for key, value in mydict.items():
    print(key, ":", mydict[key])

myfile.close()

'''
#3 Another way: Put given words in one dictionary and then
# check if upper/lower case is diff, append as a new key/value pair


mydict = {'Father':0, 'God':0, 'Christ':0, 'Spirit':0, 'life':0, 'man':0}
j={}
with open ('book of John text.txt', 'r') as myfile:
    for line in myfile:
        words = line.split()        #splits text/string into a list
        for i in words:
            if i in mydict:
                mydict[i] += 1
                if i!= i.title():   # check if first letter is lowercase
                    x = i.title()   # if yes, it as a new key to variable x
                    
                    mydict['x'] = 0     #define value of x as 0
                    mydict[x] = mydict[x]+1         #increment value of x
                    mydict[x].append(mydict[x])     #add key,value to mydict
                    
                
for key, value in mydict.items():
    print(key, ":", mydict[key])

'''

'''
#3 Another way to do this
myfile = open("book of John text.txt","r")

#store the contents of file in a variable 'book'
book = myfile.read()
myfile.close()

#initialize an empty dictionary to store contents of text file in key:value pair
word_dict ={}

#initialize a variable to 0 to store count of word's occurrances
count=0

master_text=book
#split the words in text using split() method.
indv_keys=book.split()

#using for loop to iterate through each word
for word in indv_keys:

    #using if loop to add each word to dictionary and to track the number of occurances of each lower word 
    
    if word not in word_dict:
        word_dict[word]= count+1
    else:
        word_dict[word]+=1


#Create a main dict, taking each word from the orginal text file and getting the count from lower count dictionary
#so that irrespective of the case , so that it will show the total count
main_dict={}
master_keys=master_text.split()
for word in master_keys:
     a=word
     if a in word_dict:
         main_dict[word] = word_dict[a]


print(f"Father: {(main_dict['Father'])}")
print(f"God: {(main_dict['God'])}")
print(f"Spirit: {(main_dict['Spirit'])}")
print(f"spirit: {(main_dict['spirit'])}")
print(f"life: {(main_dict['life'])}")
print(f"man: {(main_dict['man'])}")

'''



'''
#2 Working Code using list
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
