import os
import string
p = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

fp = open(p+"/The Hound of the Baskervilles Book.txt", encoding="utf8")


words=[]

lines = (line.rstrip() for line in fp) # All lines including the blank ones
lines = (line for line in lines if line) # Non-blank lines
for l in lines:
    words.append(l.translate(str.maketrans('', '', string.punctuation)).strip().split(" "))


flat_list = []
for sublist in words:
    for item in sublist:
        flat_list.append(item)

            
out=[]                

#Enter or change words to be searched here
word='<insert word>'


for j in range(len(flat_list)):
        

            if word.lower()==flat_list[j].lower():
               try:
                   if len(flat_list[j+1])<=16:
                     out.append(flat_list[j+1])

               except:
                   print("Index issue!") 
                
f = open(p+"/output.txt", "w")
for i in range(len(out)): 
 f.write(out[i]+"\n")
f.close()   
print("Results Written to output.txt file!")          

