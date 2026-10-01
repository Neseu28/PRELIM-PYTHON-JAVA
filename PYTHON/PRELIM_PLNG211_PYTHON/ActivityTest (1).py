txt = "HELLO WORLD"
print(txt[2:5])
print(txt.upper())
name = "PYTHON" 
print(f"I LOVE {name}")

print(10>9)
print(10==9)
print(10<9)

print(10>9)
print(10==9)
print(bool("Hello"))
print(bool(0))

a=15 
b=4
print(a%b)
print(a//b)
print(a**b)
print(10+a)

thislist = ["apple","banana","cherry"]
print(thislist)
print("")

thislist = ["apple","banana","cherry","apple","banana","cherry"]
print(thislist)
print("")

thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)
print("")

thislist = ["apple","banana","cherry"]
thislist.insert(1,"Maksuda Sultana")
print(thislist)
print("")

thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)
print("")

thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)
print("")

thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)
print("")

colors = ["red","green","blue"]
print(colors[0])
colors.pop(1)
del colors[0]
print(colors)
print("")

thistuple = ["apple","banana","cherry"]
print(thistuple[-1])

thistuple = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thistuple[2:5])

a=200
b=33
if b>a:
    print("b is grater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")

    age=20
    if age<13:
        print("CHILD")
    elif age<18:
        print("TEENAGER")
    else:
        print("ADULT")


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


a = 200
b = 33
if b>a:
    print ("b is greater than a")
elif a == b:
    print ("a and b are equal")
else:
    print ("a is greater than b")



a = 20
if a<13:
    print ("Child")
elif a<18:
    print ("Teenager")
else:
    print ("adult")  