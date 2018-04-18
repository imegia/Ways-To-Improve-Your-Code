#Improve your python code!

'''
1. enumerate
'''

cities = ["Marseille", "Amsterdam", "New York", "London"]

#The bad way
i = 0
for city in cities:
  print(i, city)
  i += 1

#The good way
for i, city in enumerate(cities):
  print(i, city)

#They both have the same output but the good way is easier to read

'''
2. zip
'''

x_list = [1,2,3]
y_list = [2,4,6]

#The bad way
for i in range(len(x_list)):
  x = x_list[i]
  y = y_list[i]
  print(x, y)

#The good way
for x, y in zip(x_list, y_list):
  print(x, y)

'''
3. swaping variables
'''

x = 10
y = -10
print("Before: x = {}, y = {}".format(x, y))

#The bad way
temp = y
y = x
x = temp

#The good way
x, y = y, x

print("After: x = {}, y = {}".format(x, y))

'''
4. get
'''

ages = {
  "Mary": 31,
  "Jonathan": 28,
  "Jack": 20
}

#The bad way
if "Jack" in ages:
  age = ages["Jack"]
else:
  age = "Unknown"
print("Jack is {} years old".format(age))

#The good way
age = ages.get("Jack", "Unknown")
print("Jack is {} years old".format(age))

'''
5. if in
'''

needle = "d"
haystack = ["a", "b", "c", "d"]

#The bad  way
found = False
for letter in haystack:
  if needle == letter:
    print("Found!")
    found = True
    break
if not found:
  print("Not found!")
  
#The good way
if needle in haystack:
  print("Found!")
else:
  print("Not found!")

'''
6. reading files
'''

#The bad way
f = open("text.txt")
text = f.read()
for line in text.split("\n"):
  print(line)
f.close()

#The good way
f = open("text.txt")
for line in f:
  print(line)
f.close()

#The better way
with open("text.txt") as f:
  for line in f:
    print(line)

'''
7. try, except, finally
'''

print("Converting")
try: #Won't give an error:
  print(int("1"))
except: #If there is a error:
  print("Conversion failed!")
else: #If no-except
  print("Conversion successful!")
finally: #Always - Happens regardless of the result
  print("Done!")