# #Comparing the first and last element of a single list:

# def sample(list1):
#     if list1[0]== list1[-1]:
#         return True
#     else:
#         return False

# bb = [2,3,4,5,6,7,89,0,]
# a = sample(bb)
# print(a)



# #Comparing the second and sixth elements of a single list:
# def sample (Kamiye):
#     if Kamiye[1] == Kamiye[6]:
#         return True
#     else:
#         return False

# mylist = [2,"House",3,4,5,2, 'House',7,8,9,0,2]
# asd = sample(mylist)
# print(asd)





# #Output all the characters in a string;
# kamiye = input("Enter your string:")
# for i in kamiye:
#     print(i)

#Exceptions:
def sample(Newadc):
  try:
    go = int(input("Enter your number: "))
    Newadc = go + 20
    return Newadc
  except:
    return "Not a number"
cc = sample(5)
print (cc)




