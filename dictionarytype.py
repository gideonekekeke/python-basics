# showing dictionary type representation
# declearing a variable name dictionary_name
# dictionary uses a KEY and a VALUE

dictionary_name = {
    "name":"dog",
    "age":3,
    "colour":"white"}
print(dictionary_name)


# accesing the value in a this dictionary
#using the key to get the value

print(dictionary_name['name'])



#you can also use the method  "get()" to value
print(dictionary_name.get('age'))

#changing the value of a key
dic1 = dictionary_name['colour']='black'
print(dic1)

#to check if a particular key is present in a dictionary and given it a condition if not in

if 'ballot' in dictionary_name:
    print('yes,"ballot" is one of the keys in dictionary_name')
elif 'ballot' not  in dictionary_name:
    print('no, "ballot" not a key in dictionary_name')

