#import string   

myfile = open("book of John text.txt","r")

#store the contents of file in a var called text
text = myfile.read()
myfile.close()

#  remove the punctuactions from the text
#for punctuactions in string.punctuation:
#    if  punctuactions != "-":   #added this cond to consider twenty-six/ 400-horsepower etc. as 1 word 
#        text= text.replace(punctuactions,'')
#print(text)

#initialize an empty dictionary to store  contents of  text file in key value pair format
#initialize a variable count to 0 to store  count of  word's occurrances
word_dict ={}
count=0

master_text=text
#text=text.lower()
#split the words in text using split() method.
indv_keys=text.split()

#using for loop to iterate through each words
for word  in indv_keys:

    #using if loop to add each word to dictionary and to track the number of occurances of each lower word 
    
    if word not in word_dict:
        word_dict[word]= count+1
    else:
        word_dict[word]+=1

#creating a main dict, taking each word from the orginal text file and getting the count from lower count dictionary
#so that irrespective of the case , so that it will show the total count
#for eg "No" and "no " is present in the text , we are expecting 4 as key instead of 2 for each seperate keys
main_dict={}
master_keys=master_text.split()
for word in master_keys:
     a=word
     if a in word_dict:
         main_dict[word] = word_dict[a]


print(main_dict["Spirit"])

'''
print(f"Father: {(main_dict['Father'])}")
print(f"God: {(main_dict['God'])}")
print(f"Spirit: {(main_dict['Spirit'])}")
print(f"spirit: {(main_dict['Spirit'])}")

print(main_dict["God"])
print(main_dict["Christ"])

        
#printing dictionary in readable format
choice = ["Father", "God", "Christ", "Spirit", "life", "man"]
for key,value in word_dict.items():
    if key in choice:
        print(key,":",value)
        '''

