a = ("ayooooo")                       #a is equal to the string "ayooooo"
b = (" this is my function")          #b is equal to the string, " this is my function"
 
def appendString(a,b):                #def means to define. append means to add/combine and in this case, it means to 
    return a+b                        #combine a and b. 

z=appendString(a,b)                   #z equals to combined string of a and b. 

print(z)                              #the answer 



x=input("what you want in list")        #this is another way
list = {}                              
 
def app(x):                           
    list.append(x)

app(input) 
print(list)
