# text = "welcome back in  this section "
# print(text)
# print(text[:9])
# print(len(text))

#                                                                               """"    ctrl + k  and ctrl + s   """"
# a = "######### I'm here for 10 minuts ###########"
# print (a.strip("#"))
# a = "i love learning AI and 3d graphics every day"
# print(a.title())
# print(a.capitalize())

#----------------------
# strip()   ==> remove all large spaces 
# rstrip()  ==> remove right spaces
# lstrip()  ==> remove left spaces
# title () 
# Capitalize()
# zfill(paramter)
# upper()
# lower()
# The index of the string
# split() ==> Dividing the sentence into words and display it as list & Dividing form the begining (left) default split by spacing  but you can set a parameter in this method like 
# like : split("-")
# and you can add another parameter for the number of words you want to split 
# like : split("-", 3)
# full EX: 
# A = "split in programming language used for dividing the sentence  into words like python programming."
# print(A.split(" " , 4))
# print(len(A))
# print(A.count("python", 0,))
# rsplit() ==> Dividing the sentence into words and display it as list & Dividing form the ends (right)   
# startswith() ==> if this string start with any charater that you can pathed it 
# EX: 
# charater = "s"
# print (A.startswith(charater))
# print(ord(charater)) ==> To display the ASCII  value of a character in python, you use a built in function "" ord() "". 
# This function takes a single character as an argument and return its  ASCII intger value
# replace(old value , new value , count)
# if I hava a list and I want to display  this list as string with seprator you can use  ""join()""
#EX:
# myList = ["I","am","learning","a","python","language"]
# print("-".join(myList))
#----------------------


# a, b, c, d = "1","11" ,"111" ,"1111"
# print(a.zfill(4))
# print(b.zfill(4))
# print(c.zfill(4))
# print(d.zfill(4)) 


#-----------------------    String Formating -----------------------#

# name = "Ahmed"
# age = 33
# phone = 1234
# print ("hello my name is {:s}, I'm {:d}, and my phone number is {:.3f}".format(name,age,phone)) 

# a, b, c = "one", "two", "three"
# print("Hello {0} {2} {1}".format(a, c, b ))

# firstName = "Ali"
# lastName = "Samir"

# print (f"My first name is {firstName}, and my last name is {lastName}")


#------------------------ Numbers ------------------------------------#

# a = 23
# b = (12+4j)
# c = 33.44
# d = -112
# e = -12.32
# g =  '33'
# print(type(g))
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# complexNumber = 44+99j
# print(f"this is  real part {complexNumber.real}")
# print(f"this is  real part {complexNumber.imag}")

# You  can convert form Int to float or  complex 
# You can convert form float to  int or complex
# You  can't convert form complex  to any data type

# case one
# print (100)
# print (float(100))
# print(complex(100))

# case two
# print (100.66)
# print (float(100.66))
# print(complex(100.66))

# case  three

# print (100 + 10j)
# print(int(100+10j))  ==> Error  

# myList = ["one", "two", "three", 44, True, False]

# print (myList [1:4]) 
# myList.append("five")
# print(myList)
# myList.append(33)
# myList.pop
# print (myList ) 
# print('where')

# a = [1, 22,443,1,2,545,-1212,323434,0]
# a.sort (reverse= True)
# print(a)
# a.sort (reverse= False)
# print(a)


# b =  [22,"twenty one ",  True]
# a.extend(b)
# print(a)
# aa = ["you", 'can', 'do' , 100 ,'tasks']
# aa.reverse()
# print(aa)
# # aa.clear()
# # print(aa)
# aa.insert(3 ,"on here")
# print(aa)
# aa[3] = "me"
# print(aa)


#--------------------   Tuple   ----------------------#

# myTuple = ("this"," is " , "my", "code","with","no", "misstakes",100,"my")

# print   (myTuple.count("my"))
# print   (myTuple.index("my"))
# print   (f"my is in position  {myTuple.index("my")}")



#  List []
#  Tuple ()
#  Set {}
#  Dict {}


# language = {
#     "one": "html",
#     "two" :"css",
#     "three": "python",
#     "four": "Dart"
# }

# print(language.keys() )
# print(language["three"] )

# dic  = {
#  "name":"Mouemen",
#  "age": 44,
#  "salary":22000
# }
# print(dic)
# # language = dic
# print(language)
# language ["five"] = "C#"

# print(language.values())
# language.update({"six": "Java"})
# print(language)
# -------------------  Implemetation -------------------------------#


# firstName = input("Enter your first name ").strip().capitalize()
# lastName =  input ("Enter your last name").strip().capitalize()
# email = input ("Enter your Mail").strip()
# phone = input ("Enter your phone number:").split()
# print("*"*50)
# print(f"Your Name is : {firstName} {lastName}.")
# print(f"Your Mail is :{email}")
# print(f"Your phone number is :{phone}.")
# print (f"User name  is :{email[:email.index("@")]}")
# print (f"your Domain is :{email[email.index("@") +1:]} ")



# age = int(input("Enter your age for calculate it  "))

# months = age *12 

# days = age * 365

# hours =  days * 24

# minuts = hours * 60 

# seconds = minuts * 60

# print("You lived for :")
# print(f"your  age is : {age} years")
# print(f"your  months is : {months} months")
# print(f"your  days is : {days:,} days")
# print(f"your  hours is : {hours:,} hours")
# print(f"your  minuts is : {minuts:,} munits")
# print(f"your  seconds is : {seconds:,} seconds")



# age = int(input("Please, enter your age ").strip())
# timeUnit = input("Please, Choose Time Unite: 'days' ,  'months', 'weeks' ").strip().lower()

# if timeUnit == "days":
#     print(f"Your Days is: {age*365:,}")
# elif timeUnit ==  "months":
#     print(f"Your months is:{age * 12:,}")
# elif timeUnit == "weeks":
#     print(f"Your Weeks is: {age  * 12 * 4 :,}")
# else:
#     print("sorry your choose is worng")

#------------------  Zetta system  ----------------------------#

# print("*" *90)
# print(" Welcome to ZETTA system, Your can Add and Edit your NAME ".center(90,"*"))  
# print("*" * 90)
# listNames = ["Ahmed","Sayed", "Ali", "Fouad", "Khaled"]
# name = input("Enter Your name: ").strip().capitalize()

# if name in listNames:
#     print("Success! Your name in the system \nChoose  your accessabilty Delete or Edit")
#     action = input("what\'s your choosise: ").strip().capitalize()
#     if action == "Delete":
#         print(f"this list before Delete: {listNames}")
#         listNames.remove(name)
#         print(f"this list After Delete: {listNames}")
#         # print(listNames)
#     elif action == "Edit":
#         newName = input("Enter the  New Name: ").strip().capitalize()
#         listNames [listNames.index(name)] = newName
#         print(listNames)
# elif name not in  listNames:
#     print("Sorry your name isn't in the system 😞, \nbut you can add your name in the system:")
#     print("If you want, Enter your name; else enter thanks")
#     giss = input ("What\'s your chooise:  ").strip()
#     if giss == "thanks":
#         print("Thank you for using this system:".center(60,"*"))
#     else:
#         listNames.append(giss)
#         print(f"this list After Delet: {listNames}")
        #---------------------  Sort and Display the list -------------#
# myFavouriteWibs = []
# print("*" *80)
# print(" Welcome to Bookmark list  ".center(80,"*"))
# print("*" *80)
# maxWibs = int(input("Enter the Mixmum of wibs:  "))
# while maxWibs > 0 :
#     wibName = input("Please enter the wibesite name: ").strip().lower()
#     myFavouriteWibs.append(f"https://{wibName.strip().lower()}")
#     maxWibs-=1
#     print(f"Wibsite added, {maxWibs} Plsces left")
#     print(myFavouriteWibs)
# else:
#     print("Bookmark is full, you can't add any more")


# display = input("To distplay enter yes else enter no: ").strip().lower()
# if display == "yes" or display  == "y":
#     print("Printing the list of BookMark.... ")
#     index = 0

#     if len(myFavouriteWibs) > index:
#         myFavouriteWibs.sort()
#         while index < len(myFavouriteWibs):
#             print(myFavouriteWibs[index])
#             index += 1
# else :
#     print("Exit")

#------------------------ Guss the password ------------------#
print("%" * 60)
print(" Hello, Welcome To Guss  Password Game  ".center(60, "%"))
print("%" * 60)



