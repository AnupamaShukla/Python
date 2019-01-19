

# wap to accept 3 numbers from user and print minimum of them

print("Enter 3 numbers : ")
num1,num2,num3 = eval (input ())

if num1 < num2 and num1 < num3 :

    print ("Minimum is : " + str(num1))

elif num2 < num3 :
    print ("Minimum is : " + str(num2))

else:
    print ("Minimum is : " + str(num3))

