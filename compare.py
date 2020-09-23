


a = 2
b = ""
print((str(a) + b))



a = "nigeria"
b = "uganda"
nigeria = 6000
uganda = 2000
print(nigeria % uganda)


x = 3
y = 5
print(y|3)


x = 4
print(x<4 or x>3)


x = ["apple","banana"]
y = ["apple","banana"]
z = x
print(x is z)       #identity operation compare if both variable are the same object
print(x is y)       #identity operation compare if both variable are the same object
print(x is not y)   #identity operation compare if both variable is not same object
print("apple" in x ) #membership operation is use to test if a perticular sequence is present  in an object










#to add an item in a list u use list.append
list = ['apple','banana','cherry']
list.append('beans')
print(list)


x = ['apple','banana','cherry']
y = ['apple','banana','cherry']
x.append('yam')#to add a list
x.remove('banana')# to remove a list

print(x)
z = x + y #joinig two list
print(z)

x.clear()
print(x)
x = (('beans','pepper','kashew',))
print(x)