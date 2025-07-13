from re import S
from secrets import randbelow




x=5
print(type(x))
x="hellow wolrd"
print(type(x))
x=bool (5) 
print(x)
print(type(x))
x=memoryview(bytes(5))
print(x)
print(type(x))
x=range(6)
print(x)
print(type(x)) 
x=(5844)
print(type(x))
if 54 > 24:
    print('fifty four is greter than twenty four')
    print("twenty four is less than fifty four")
New_car=('lamboginy')
print(New_car)
titile=('david`s investment')
print(titile)
x=1   #int
y=2.8 #float
z=1j  #complex
print(type(x))
print(type(y))
print(type(z))
x=1             # int or integer
y=35656222554887711
z=-3255522
print(type(x))
print(type(y))
print(type(z))
x=1.10        # floats or floating point numberse
y=1.0
z=-35.59
print(type(x))
print(type(y))
print(type(z))
x=35e3      #float can also be scientific number with an e to indicate the power of 10
y=12e4
z=-86.7e100
print(type(x))
print(type(y))
print(type(z))
x=3+5j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))
x=1
y=2.8
z=1j
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c) 
print(type(a))
print(type(b))
print(type(c))
x=int(1)   # x will be 1
y=int(2.8)  # y will be 2
z=int("3")  # z will be 3
print(x)
print(y)
print(z)
x=float(1)  # x will be 1.0
y=float(2.8)  # y will be 2.8
z=float("3")  # z will be 3.0
w=float("4.2")  # w will be 4.2
print(x ,y ,z,w )
x=str("s1")
y=str(2)
z=str(3.0)
print(x ,y ,z)
# python strings
print("hello ")#double quotation or
print('hello') #single quotation
#quotes inside quotes
print("lt`s alright")
print("he is called 'johnny'")
print('he is called "johnny"')
#Assing string to a variable
a="hello"
print(a)
#Multiline strings
a="""lore ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididuntut
labore et dolore magna aliquq."""
print(a)
#looping throug a string
for x in "banana":
    print(x)
    a="hellow, world!"
    print(len(a))
    txt="The best thing in life are free!"#check string
    print("free" in txt)
    txt="The best thing in life are free!"#if statement
if"free" in txt:
    print("yes, 'free' is present.")
    # check if not
    txt="The best thing in life are free!"
    print("expensive" not in txt)
    txt="The best thing in life are free!"
    if "expensive" not in txt:
        print("NOT, 'expensive' is NOT present.")
b="hello, world!"# slicing strings
print(b[2:5])
b="hello, world!"
print(b[:5])
b="hellow, world!"
print(b[2:])
b="hellow, world!"
print(b[-5:-2])
# modify strings
a="helow world!" # upper case
print(a.upper())
a="hellow david"# lower case
print(a.lower())
a="Hellow, world!"  # remove whitespace  stip()
print(a.strip())  # returns "Hellow worid"
a="Hellow, world!"#relace string
print(a.replace("H", "J"))
a="Hellow, world!"
print(a.split(","))   # returns ['Hellow', 'world!']
a="hello" # concatenate strings
b="world"
c= a + b
print(c)
a="Hello"
b="world"
c= a + " " + b
print(c)
# format strings 
age=36  # use of f-strings and {}
txt=f"my name is David, I am {age}"
print(txt) 
price=59 # placeholders and modifiers
txt=f"The price is {price} dollars"
print(txt)
price=69 # use of 2f as 2 decimals
txt=f"The price is {price:.2f} dollars"
print(txt)
txt=f"The price is {20 * 59} dollars"# python code, math operation
print(txt)
# Escape characters :
txt="we are the so-called \"vikings\"from the north."
print(txt)
# python Booleans :
print(10 > 9) # true
print(10==9)  # false
print(10 < 9) # false
a=200
b=33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print(bool("Hellow"))
print(bool(15))

x="Hello"
y=15
print(bool(x))
print(bool(y))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "bannanas"]))
class myclass():
    def _len_(self) :
        return 0
myobj=myclass()
print(bool(myobj))
#functions can reton boolean
def myfunction():  #true/YES!
    return True
if myfunction(): 
    print("YES!")
else:
    print("NO!") 

x=200
print(isinstance(x, int))
print(5+4-7+3)
print(bool(45))
if 6 < 12:
  print("six is less than twelve")
  print("twelve is greater than six")

# python Lits
thislist=["appple", "banana", "cherry"]
print(thislist)
thislist=["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # allow duplicates
print(len(thislist))
thislist=["apple", "banana", "cherry"]
print(len(thislist)) #list length 3
list1=["apple", "banana", "cherry"]
list2=[1, 5, 9, 3]
list3=[True, False, False]
print(list1)
print(list2)
print(list3)
list1=["abc", 34, True, 40, "male"]
print(list1)
mylist=["apple", "banana", "cherry"]
print(type(mylist))  #type() <class 'list'>
thislist=list(("apple", "banana", "cherry")) # not the double round-brackets
print(thislist)
#python-Access lit items
thislist=["apple", "banana", "cherry"]
print(thislist[1]) # banana is [1]
print(thislist[0])  # apple is [0]
thislist=["apple", "banana", "cherry"] #negative indexing
print(thislist[-1]) # -1 refers to the last item
print(thislist[-2]) # -2 refers to the second last item
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # from apple to orange
# Range of Negative Indexes
thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # start from orange kiwi and melon
thislist=["apple", "banana", "cherry"]
if "apple" in thislist:  # to determine if a specified item is present in a list use the in keyword
    print("yes, 'apple' is in the fruits list")
#change list items
thislist=["apple", "banana", "cherry"] #change item value
thislist[1]="blackcurrant"#change banana to blackcurrant
print(thislist)
thislist=["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3]=["blackcurrant", "watermelon"]
print(thislist) # change banana:1 to blackcurrant and cherry:3 to watermelon
thislist=["apple", "banana", "cherry"]
thislist[1:2]=["blackcurrant", "watermelon"]
print(thislist)
thislist=["apple", "banana", "cherry"]
thislist[1:3]=["watermelon"]
print(thislist) #['apple', 'watermelon',]
thislist=["apple", "banana", "cherry"]
thislist.insert(2,"watermelon") # inser to the list using inset() method
print(thislist)# should not containe 4 items in the list
#python -add list items:
#Add an item to the end of the list, use the append() method
thislist=["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist=["apple", "banana", "cherry"] # insert() method 
thislist.insert(1, "orange")
thislist=["apple", "banana", "cherry"]
tropical=["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)     
thislist=["apple", "banana", "cherry"]
thistuple=["kiwi", "orange"]
thislist.extend(thistuple)
print(thislist)
#Remove List Items 
thislist=["apple", "banana", "cherry"] #remove specified items using remove()
thislist.remove("banana")
print(thislist)
thislist=["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") # removes the first item with the same mame
print(thislist)
thislist=["apple", "banana", "cherry"]#remove specified index
thislist.pop(1)
print(thislist)
thislist=["apple", "banana", "cherry"]
thislist.pop() # removes the last item in the list
print(thislist)
thislist=["apple", "banana", "cherry"]
del thislist[0] #del removes specified index
print(thislist)
thislist=["apple", "banana", "cherry"]#Clear the list
thislist.clear()# The list stil remains, but it has no comtent
print(thislist)
# Loop through a list
thislist=["apple", "cherry","banana"]
for x in thislist:
    print(x)
thislist=["banana", "apple", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
thislist=["apple", "bananan", "cherry"]
i=0
while i <len(thislist):
    print(thislist[i])
    i=i+1
thislist=["apple", "banana", "cherry"]
[print(x)for x in thislist]
thislist=["apple", "banana", "cherry"]
i=0
while i < len(thislist):
    print(thislist)
    i=i+1
thislist=["cherry", "apple", "banana"]
[print(x) for x in thislist]

# list comprehension
fruits=["apple", "banana", "cherry", "kiwi", "manog"]
newlist=[]

for x in fruits:
    if "a" in x:
      newlist.append(x)
print(newlist)

thislist=["banana", "apple","cherry"]
print(thislist)
fruits=["apple", "banana", "cherry", "kiwi", "mango"]  # listing all the items with the letter "a" on the list using for
newlist=[x for x in fruits if "a" in x]
 
fruits=["apple", "banana", "cherry", "kiwi","mango"]
newlist=[x for x in fruits if x !="apple"]# if x !="apple" will return true making the list to contain all fruits except "apple"
print(newlist)
newlist=[x for x in range(10)] #range() make iterable:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
print(newlist)
newlist=[x for x in range(10) if x <5]# makes [0, 1, 2, 3, 4]
print(newlist)
fruits=["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x.upper() for x in fruits]
print(newlist)
fruits=["apple", "banana", "cherry", "kiwi", "mango"]
newlist=['hello' for x in fruits] # will change all the items on the list to hello
print(newlist)
fruits=["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x if x !="banana" else "orange" for x in fruits]
print(newlist)# will change "banana" to"orange"
# sort lists
thislist=["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #sort() method that will sort the list alphanumerically,ascending
print(thislist)
thislist=[100, 50, 65, 82, 23]
thislist.sort() # sort()arranges in orde of numericall [23, 50, 65, 82, 100]
print(thislist)
thislist=["orang", "mango", "kiwi", "pineapple" "banana"]
thislist.sort(reverse= True)#arranges from backwords
print(thislist)
thislist=[100, 50, 65, 82, 23]
thislist.sort(reverse= True)# arranges [100, 82, 65, 50, 23]
print(thislist)
def myfunc(n):
    return abs(n -50)
thislist.sort(key = myfunc)
print(thislist)
thislist=["banana", "orange", "kiwi", "cherry"]
thislist.sort (key = str.lower)
print(thislist)
thislist=["banana", "orange", "kiwi", "cherry"]
thislist.reverse()
print(thislist)
# copy lists
thislist=["apple", "banana", "cherry"]
mylist=thislist.copy()
print(mylist)
thislist=["apple", "banana", "cherry"]
mylist=list(thislist) # use the list() method list()
print(mylist)
thislist=["apple", "banana", "cherry"]
mylist=thislist[:]  # use of a slice operator :
print(mylist)
#join two lists
list1=["a", "b", "c"]# join by using +
list2=[1, 2, 3]

list3=[list1+list2]
print(list3)
list1=["a", "b","C"]# join by use of appending
list2=[1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)    
list1=["a", "b", "c"]
list2=[1, 2, 3] # join by the use of extend()

list1.extend(list2)
print(list1)
#PYTHON TUPLES
thistuple=("apple", "banana","cherry")
print(thistuple)
thistuple=("apple", "banana", "cherry")
print(len(thistuple)) # tuple length using len() 3
thistuple=("apple",)
print(type(thistuple))
# Not a tuple
thistuple=("apple")
print(type(thistuple))
tuple=("apple", "banana", "cherry")
tuple=(1, 5, 7, 9, 3)
tuple=(True, False, False)

mytuple=("apple", "banana", "cherry")
print(type(mytuple))
thistuple=("apple", "banana", "cherry")
print(thistuple[1]) # 0 index is apple 1 index is banana
print(thistuple[-1]) # -1 index refers to the last item on the list cherry
thistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # index (3, 4, 5)in the list
print(thistuple[:4]) # index (1, 2, 3, 4,) will be in the list
print(thistuple[2:]) # index (1, 2, 3, 4, 5,) will be on the list exipt index (6, 7)
# Range of negative indexes 
thistuple=("apple", "banana", "cherry")
if "apple" in thistuple: # check if item exists using in keyword
    print("yes, 'apple' is in the fruits tuple")
# update tuples
x=("apple", "banana", "cherry")
y=list(x)
y[1]="kiwi"
x=(y) 

print(x)

thistuple=("apple", "banana", "cherry")
y=list(thistuple)
y.append("orange")
thistuple=(y)

thistuple=("apple", "banana", "cherry")
y=("orange",) # will be added as the last item on the tuple
thistuple +=y
print(thistuple)
# Removing items
thistuple=("apple", "banana", "cherry")
y=list(thistuple)
y.remove("apple") # removed apple on the tuple using remove() key
thistuple=(y)
print(thistuple)
# unpack tuples
fruits=("apple", "banana", "cherry")
(green, yellow, red)=fruits
print(green) # this is extracting a value back into the variable
print(yellow)
print(red)
fruits=("apple", "banana", "cherry", "strawberry", "mango")
(green, yellow, *red)=fruits # using Asterisk *
print(green) # assignig * to the variable as a list
print(yellow)
print(red)
 
fruits=("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red)=fruits
print(green)
print(tropic)
print(red)
# loop through a tuple using for
thistuple=("apple", "banana", "cherry")
for x in thistuple:
   print(x)
thistuple=("apple", "banana", "cherry")
for i in range(len(thistuple)): #loop through the index numbers using range() and len() functions
   print(thistuple[i])
thistuple=("apple", "banana", "cherry")
i=0
while i < len(thistuple):
    print(thistuple[i])
    i=i+1
# join two tuples  
tuple1=("a", "b", "c")
tuple2=(1, 2, 3)
tuple3=tuple1+tuple2 # joining tuples by using +
print(tuple3)
fruits=("apple", "banana", "cherry")
mytuple=fruits *2
print(mytuple)
# PYTHON SETS
thisset={"apple", "banana", "cherry"}
print(thisset) # you cannot change its items, but you can remove items and add new items
thisset={"apple", "banana", "cherry", "apple"}
print(thisset) # Dupicate values will be ignored
thisset={"apple", "banana", "cherry", True, 1, 2}
print(thisset) # True and 1 are considered the same value in set and are treated as duplicates
thisset={"apple", "banana", "cherry", False, True, 0}
print(thisset) # False and 0 is considered the same value
thisset={"apple", "banana", "cherry"}# geting the length of  set using len() function
print(len(thisset))
myset={"apple", "banana", "cherry"}
print(type(myset)) # to get data type
thisset=set(("apple", "banana", "cherry"))
print(thisset) #set() fuction can be used to constructor to make a set
thisset={"apple", "banana", "cherry"}
for x in thisset:
   print(x)
thisset={"apple", "banana", "cherry"}
print("banana" in thisset) #check if "banana" is present in the set banana True
thisset={"apple", "banana", "cherry"}
print("banana" not in thisset) # check if "banana" is NOT present in the set banana false
thisset={"apple", "banana", "cherry"}
thisset.add("orange") # use the add() method to add an item to a set
print(thisset)
thisset={"apple", "banana", "cherry"}
tropical={"pineapple", "mango", "papaya"}
thisset.update(tropical) # to add another set into the current set, using the update() method
print(thisset) # Add elements from tropical into thisset
thisset={"apple", "banana", "cherry"}
mylist=["kiwi", "orange"] #the update() method can add both tuples , list, set and dictionaries
thisset.update(mylist)
print(thisset)
#Remove Set Items
thisset={"apple", "banana", "cherry"}
thisset.remove("banana") # use the remove() fuction
print(thisset) # remove() will raise an error if the item to remove does not exist
thisset={"apple", "banana", "cherry"}
thisset.discard("banana") # use the discard() method to remove an item from a set
print(thisset) # will not raise an error if the item to remove does not exist
thisset={"apple", "banana", "cherry"}
x=thisset.pop() # set are unordered, so when using the pop () method, you do not know which item that gets removed
print(x)
print(thisset)
thisset={"apple", "banana", "cherry"}
thisset.clear() # clear() method empties the set
print(thisset)
thisset={"apple", "banana", "cherry"}
del thisset # del () keyword   will delete the set completely
# loop items
thisset={"apple", "banana", "cherry"}
for x in thisset:
   print(x)
# join set
set1={"a", "b", "c"}
set2={1, 2, 3}
set3= set1.union(set2)# union() method join set set1 and set2 into a new set
print(set3)
set1={"a", "b", "c"}
set2={1, 2, 3}
set3=set1 | set2 # you can use | operator instead of the union() method
print(set3)
 # join multiple set
set1={"a", "b", "c"}  
set2={1, 2, 3}
set3={"john", "Elena"}
set4={"apple", "banana", "cherry"}
# join multiple set with the union() method:
myset=set1.union(set2, set3, set4)
print(myset)

set1={"a", "b", "c"}
set2={1, 2, 3}
set3={"apple", "banana", "cherry"}
set4={"john", "Elena"}
myset=(set1 | set1 |set2 |set3 | set4)
print(myset)
x={"a", "b", "c"} # join a set with a tuple: using union() method
y=(1, 2, 3)
# the | operator only allows you to join sets with sets, and not with other data types like youcan with the union() method
z=x.union(y)
print(z)
set1={"a", "b", "c"}
set2={1, 2, 3}
set1.update(set2) # update method to inset the items in set2 into set1
print(set1)
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
set3=set1.intersection(set2)# intersection will join only items in both sets
print(set3)
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
set3=set1 & set2 # ues & instead of instersection() method
print(set3)# & and intersection() are used to join sets with other sets but not with other data types
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
set.intersection_update(set2)
print(set1)# keep the items that exist in both set1 and set2
#Difference ()
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
set3=set1.difference(set2) # keep all items from set1 that are not in set2
# using - operstor insted of the difference() method and you will get the same result
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
set3=set3 - set2 # use - to join two sets
print(set3)# - and difference() joins sets with sets and not ather data type
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1) # use the difference_update() method to keep the items that are not present in both sets
  
set1={"apple", "banana", "cherry"}
set2={"google", "microsoft", "apple"}
set3=set1.symmetric_difference(set2) # this method will keep only the elements that are not present in both sets
print(set3)
# ^ operator joins sets with sets but not with other data typeslike you can with the symmetric_ifference() method
set1={"apple", "banana", "cherry"}
set2={"google",  "microsoft", "apple"}
set3=set1 ^ set2
print(set3)

set1={"apple", "banana", "cherry"}
set={"google", "microsoft", "apple"}
set.symmetric_difference_update(set2) # this method is used to keep the items that are not [resent in both sets:]
print(set1)
# PYTHON DICTIONARIES
# dictionaries are written with curly brackets, and have keys and values:
# dictionary items are orded, changeable, and do not alllow duplicates.
thisdict={"brand":"ford",
          "model": "mustang",
          "year":1964
}
print(thisdict)
thisdict={"brand":"ford",  # 
          "model":"mustang",
          "year":1965
}
print(thisdict["brand"]) # dictionaries cannot have two items with the same key:
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1966,
    "year":2020,
}
print(thisdict) # Dupicate values will overwrite existing:

print(len(thisdict)) #print the number of items in the dictionary
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(type(thisdict)) # print the data type of a dictionary:using the function type()

thisdict=dict(name="james", age=36, country="Norway")
print(thisdict) # using the dict() method to make a dictionary:
thisdict={
     "brand":"ford",
     "model":"mustang",
     "year":1967
 }
x=thisdict["model"]
print(x)
y=thisdict.get("brand") # get() function to Get the value of the "model" key:
print(y)
car={
    "brand":"ford",
    "model":"mustang",
    "year":1987
}
x=car.keys()
print(x) # befor the change
car["color"]="white"
print(x) #after the change

car={
    "brand":"ford", 
    "model":"mustang", 
    "year":1977
}
x=car.values()  
print(x)# before the change
car["year"]=2020
print(x) # after the change

car={
    "brand":"ford",
    "model":"toyota",
    "year":1999
}
x=car.values() #add a new item to the orginal dictionary
print(x)
car["color"]="red"
print(x)

thisdict={
    "brand":"ford", 
    "model":"mustang",
    "year":1964
}
if "model" in thisdict:# check if "model" is present in the dictionary 
    print("yes, 'model' is one of the keys in the thisdict dictionary")

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1954
}
thisdict["year"]=2018 # change the value of a secific item by referring to its key name
print(thisdict)# change the "year" to 2018
thisdict.update({"year":2027})
print(thisdict)
# Removing items
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1944
}
thisdict.pop("model") # the pop() method removes the item with the seoecified key name:
print(thisdict)

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1912
}
thisdict.popitem()# this method removes the last inserted item popitem()
print(thisdict)

thisdict={
    "brand":"totota",
    "model":"mustang",
    "year":1964
}
del thisdict["model"] #del keyword removes the item with the specified key name:
print(thisdict)

thisdict.clear() # this method clear() empties the dictionary:
print(thisdict)
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":2000
}
for x in thisdict: # this method is used to print dictionary, one by one:
    print(x)
thisdict={
    "brand":"isuzu",
    "model":"truck",
    "year":2023
}
              
for x in thisdict.values(): # used to return values of a dictionary
    print(x)
thisdict={
    "brand":"totota",
    "model":"van",
    "year":2021
}
for x in thisdict.keys(): # used to return the keys of a dictionary:
   print(x)
# copy Dictionaries
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
mydict=thisdict.copy() # make a copy of a dictionary with the copy() method
print(mydict)
thisdict={
    "brand":"isuzu",
    "model":"truck",
    "year":1919
}
mydict=dict(thisdict) # make a copy of a dictionary with the dict() function:
print(mydict)
# Nested Dictionaries
myfamily={
    "child1":{
        "name":"Emil",
        "year":2004
    },
    "child2":{
        "name":"Tobias",
        "year":2007
    },
    "child3":{
        "name":"linus",
        "year":2011
    }
}
print(myfamily)

print(myfamily["child2"]["name"])
 # PYHON IF ... ELSE

a=33
b=200
if b>a:
  print("b is greater than a")
# Elift
a=42
b=42
if b>a:
    print("b is greater than a")
elif a == b:  # this method is used to now if the previous were not true, the try this condition
    print("a and b are equal") 

a=200
b=33
if b>a:
    print("b is greater than a")
elif a ==b:
    print("a and b are equal")
else:
    print("a is gerater han b")
    
a=200
b=33
if b>a:
   print("b is greater than a")
else:
    print("b is not greater than a")

a = 2 
b = 330
print("A" if a>b else print("B")) # one line if else statement
a=330
b=330
print("A") if a>b else print("=") if a == b else print("B")
a=200
b=33
c=500
if a>b and c>a: # the and keyword is a logical operator and is uesd to combine conditional statements:
    print("both conditions are true") 
a=200
b=33
c=500
if a>b or a>c:  # or keyword is a logical operator, and is used to use to combine conditional statements:
    print("At least one of the conditions is True")

a=33
b=200
if not a>b:# not keyword is a logical operation, and is used to reverse the result of the conditional statement
    print("a is NOT greater than b")
x=41

if x>10:
    print("Above ten,")
    if x>20:
        print("and also above 20!")
    else:
        print("but not above 20.")

a=44
b=200

if b>a:
    pass

# PYTHON MATCH
day=4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thusady")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("sunday")

day=4 
match day: # _ as the last case if you want a code block to execute when there are not other matches:
    case 6:
        print("Today is saturday")
    case 7:
        print("Today is sunday")
    case _:
         print("looking forward to the weekend")

day=4
match day:
    case 1 | 2 | 3 | 4 | 5 :
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

month=5
day=4
match day:
    case 1 | 2 | 3 | 4 | 5 if month ==4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 4 | 5 if month ==5:
        print("A weekday in may")
    case _:
        print("No match")

#  PYTHON WHILE LOOPS
i=1
while i < 6: # print i as long as i is less than 6
    print(i)
    i+=1

i=1
while i<6:
    print(i)
    if i == 3: # exit the loop when i is 3:
        break  # break statement we can stop the loop even if the while condition is true:
    i+=1

i=0
while i<6:
    i += 1
    if i == 3:
        continue # continue to the next iteration if i is 3:
    print(i)

i=1
while i<6:
    print(i)
    i+=1
else: # print a message once the condition is false:
    print("i is no longer less than 6")

# PYTHON FOR LOOPS
fruits=["apple", "banana", "cherry"]
for x in fruits: # print each fruit in a fruit list:
    print(x)
for x in "banana": # loop through the letters in the word "banana"
    print(x)

fruits=["apple", "banana", "cherry"]
for x in fruits:
    print(x) # exit the loop when x is "banana"
    if x == "banana":
        break 
    print(x)

fruits=["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana": # do not print banana:
        continue
    print(x)
for x in range(6):
    print(x) # not that rangr(6) is not the values of 0 to 6, but the values 0 to 5.

for x in range(2, 6): # using the start parameter:
    print(x) # print 2 3 4 5 but not including 6

for x in range(2, 30, 3): # increment the sequence with 3(default is 1):
    print(x)

for x in range(6):
    print(x)
else: # else block wil NOT be executed if the loop is stopped by a break statement
    print("Finally finished!")

for x in[0, 1, 2]:
    pass # pass statement to avoid getting an error.
print(x)

# PYTHON FUNCTIONS
def my_function(): # python a function is defined using the def keyword:
    print("Hello from a function") 

def my_function(): # To call a function, use the function name followed by parenthesis:
    print("Hellow from a function")
my_function()

def my_function(fname):
    print(fname+ "Refsnes")

my_function("Emil" )
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname): # this function expects 2 arguments, and gets 2 arguments:
    print(fname + " " + lname)
my_function("Emil", "Refsnes") # if you try to call the function with 1 or 3 arguments, you will get an error:

def my_function(*kids): # if the number of arguments is unknwn, add a * before the parameter name:
    print("The youngest child is " + kids[2]) # 2 is linus becouse 0 is Emil and 1 is Tobias
my_function("Emil", "Tobias", "linus")

def my_function(child3, child2, child1):
    print("The youngest child is " + child3) # linus is the youngest child
my_function(child1="Emil", child2="Tobias", child3="Linus")

def my_function(**kid): # will recive a dictonary of arguments, and can access the items accordingly:
    print("His last name is " + kid["lname"])
my_function(fname="Tobias", lname = "Refsnes")

def my_function(country="Norway"): # if we call the function without argument, it uses the default value:
    print("I am from " + country)
 
my_function("sewden")
my_function("india")
my_function() # Norway
my_function("Brazil")

def my_function(food):
    for x in food:
        print(x)
fruits=["apple", "banana", "cherry"]
my_function(fruits)

def my_function(x):
    return 5 * x  # To let a function return a value, use the return statement:

print(my_function(3)) # 5*3=15
print(my_function(5)) # 5*5=25
print(my_function(9)) # 5*9=45

def my_function(x, /): 
    print(x) # 3
my_function(3)

def my_function(x):
    print(x)
my_function(x=3) #3

def my_function(*, x):# function can have only keyword arguments
    print(x)
my_function(x=3) #3

def my_function(k):
    if(k>0):
        result=k + (k - 1)
        print(result)
    else:
        result=0
    return result
print("Recursion Example Results:")

# PYTHON LAMBDA

x=lambda a : a + 10 # Add 10 to argument a, and return the result:
print(x(5)) # 10+5=15

x=lambda a, b : a * b # multiply argument b and return the result
print(x(5, 6)) # 5*6=30

x=lambda a, b, c : a + b + c # summarize argument a, b, and c and return the result:
print(x(5, 6, 2)) # 5+6+2=13

def myfunc(n):
    return lambda a : a * n
mydoubler=myfunc(2) # use the function definition to make a function that always triples the number you send in:
print(mydoubler(11)) # 11*2=22

def myfunc(n):
    return lambda a : a * n
mydoubler=myfunc(2) # use the same function definition to make both function, in the same program:
mytripler=myfunc(3)
print(mydoubler(11)) #11*2=22
print(mytripler(11)) # 11*3=33

# PYTHON ARRAYS
cars=["ford", "volvo", "bmw"] # looping array elements
for x in cars:
    print(x)

#PYTHON CLASSES AND OBJECTS
# To create a class, use the keyword class:
class myclass: # create a class named myclass, with a property named x
    x=5

p1=myclass() # create an object named p1, and print the value of x:
print(p1.x) # 5

# The_init_()Function

class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

p1=person("john", 36)

print(p1.name) # john
print(p1.age) # 36

class person:
    def __init__(self, name, age):
        self.name=name
        self.aage=age

p1=person("john", 36)
print(p1)

class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}{self.age})"
p1=person("John", 36)
print(p1)

class person:
    def __init__(self, name, age): # insert a function that prints a greeting, and execute it on the p1 object:
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is " + self.name)  #  printing Hello my name is john
p1=person("John", 36)
p1.myfunc()       

class person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name=name
        mysillyobject.age=age
    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1=person("johnson", 36)
p1.myfunc()        
 # PYTHON INHERITANCE
class person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)

x=person("David", "MWaura")
x.printname()
        























