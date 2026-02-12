x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(x > 0 and x < 10)

x = 5
print(x < 5 or x > 10)

x = 5
print(not(x > 3 and x < 10))

#identity
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)


x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)


#membership
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

#bitwise
print(6 & 3)

#presedence oeprator
print((6 + 3) - (6 + 3))