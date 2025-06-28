from traceback import print_exc


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











































