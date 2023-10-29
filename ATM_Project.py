#ATM process
#Assumption is Card and Pin Verification is already done
import random
from datetime import datetime
balance=random.randint(0,10000)
statement_msg=""
while True:
    print("1. Account Balance")
    print("2. Withdrawal your amount")
    print("3. Transfer from one to other")
    print("4. Mini Statement")
    print("5. Exit")

    ch = input("Enter your option")
    if ch=="1":
        print("Here is your account balance:")
        #print(datetime.now(),":INR Amount is",balance)
        print(datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),":INR IS",balance)
    elif ch=="2":
        amount = int(input("Enter the amount to withdraw"))
        if amount < balance:
            dttm = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            statement_msg += "\n" + str(dttm) + ": Withdrawal made of Rs." + str(amount)
        # '''if amount>balance:
        #     print("you don't have sufficient balance. Enter another value")
        # else:
        #     balance = balance-amount
        #     print("Pls collect your cash")'''
        # #Note:  Python also provides one line condition when dealing with one action.

        # output = "you don't have sufficient balance. Enter another value" if amount>balance else balance-amount
        output = balance if amount > balance else balance - amount
        msg = "You don't have sufficient balance" if amount>balance else "Pls collect the cash"
        print(msg)
        balance=output
    elif ch=="3":
        amount = int(input("Enter the amount to transfer"))
        if amount<balance:
            dttm = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            statement_msg += "\n"+str(dttm)+ ": Transfer made of Rs."+str(amount)
        output = balance if amount > balance else balance - amount
        msg = "You don't have sufficient balance" if amount > balance else "Your amount has been transeferred"
        print(msg)
        balance = output
    elif ch=="4":
        dttm = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        statement_msg+= "\n Total balance as of now on "+str(dttm) +" is "+ str(balance)
        print(statement_msg)
    elif ch=="5":
        print("THANKS & HAVE A NICE DAY AHEAD!")
    else:
        print("I did not understand your choice pls try again")
        exit()
        #statemment_msg is empty first time so that it can track every step of each statement.

        #Assignnemnt : Add logic for deposit like more than 10,000 deposit will be rejected else done.
        #Just like we have one line if, else same we have one line loop also.

str1  = "HELLO"
str2 = "THEREU"
print(str1+str2)
print("Number of character = ",len(str1))
print("Number of character = ",len(str2))
print(str2+ " "+str1+" "+str(7))
#Note: String added with string only no interger (No number).
#if numbers to be added with string, need to put str (5)any number in the bracket.
print(str1*5)
print(str2*5)
print((str2+" ")*5)
print(str1+" "*7)

for counter in range(10):
    print("*",end=" ") #This is one way

print("\n---------------")

print("* "*10)# This is another way to print * like that.
print()
for counter in range(5):
    print("* "*10)
print()
for counter in range(1,7):
    print("* "*counter)
#Python is a case sensitive language.
#for numbers we are using range and for text we use string(str)
str3="HelLOo"
for i in str3:
    print(i)
    print("--------")
for i in range(len(str3)):
    print(i)
    print()
    print(str3[2])
str4 = "Hyderabad"
for i in range(len(str4)):
    # print(f"The character position of {i} is {str4[i]}")
    print(str4[i])
    print("----------")
str5 = "Mahendra"
lenght=len(str5)
print(str5[-1]), "&", print(str5[-4])
print(str5[lenght-1])

#Immutatble means you can not edit
#and this is all about indexing the characters and how to do that?
str1  = "hello"
#str1[0] = "H" This is not possible
#print(str1[0])
#TypeError: 'str' object does not support item assignment
#But we can change the whole value of str1
str1 = "AB H"+str1[1:5] #str1 = "H"+str1[1:5]
print(str1) #It means we can not edit it but we can overwriting it.
str2 = "Mahi"
print(str2[-1:-4])
str3 = "Hello There"
#This is for initial four characters
print(str3[0:4], str3[:4], str3[-len(str3):-len(str3)+4]) #last character would be len of str-1
#Now for last 4 characters
print(str3[len(str3)-4:len(str3)], str3[len(str3)-4:], str3[-4:])

str1 = "Hello There"
#I am creating an object of class string.
# It will get all the properties that are defined for a class.
str1 = "a"
print(str1.isspace()) #False
str1  = "      "
print(str1.isspace())# True  This is used to check space or any character there.

length = input("Enter the length of the rectangle")

if length.isdigit():
    length = int(length)
    print("length is ",length)
else:
    print("Not a valid number")
    exit()

    # This is to use to check what user has entered as input and gracefully,
    # we are removing the error and close the program even if user entered a invalid number.

#Hell Hell Hell
#here here here