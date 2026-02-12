def func (name) :
  print ("hello", name)
func ("radit")

def get_greeting():
  return "Hello from a function"
message = get_greeting()
print(message)

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)
print(factorial(5))