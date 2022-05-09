# x = [12,123,34,45,34,240,31,1,5,8,900000000000000000000000000]
# print (x[5]+x[10])

def sample(a,b):
    try:
        Kamiye = (a/b)
    except ZeroDivisionError as e:
        return "Any number divisible by zero is undefined"
    else :
        return "The given division is:", Kamiye

abc = sample(25,25)
print(abc)


def sample(k):
    try:
        Kamiye = int(input("Enter a number:"))
    except Exception:
        return "Invalid input"
    else :
        return Kamiye

print (sample(7))

#Add 20 to a number\exception handling.
def sample(two):
    try:
        Kamiye = two + 20
    except TypeError:
        return  'Wrong input'
    else:
        return Kamiye
         
adc = sample(67)
print("Th result is:",adc)


#Exception handling\Request for input and add 20 to the result:
def sample(Newadc):
  try:
    go = int(input("Enter your number: "))
    Newadc = go + 20
    return Newadc
  except:
    return "Not a number"
cc = sample(5)
print (cc)