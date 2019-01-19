

# wap to accept string from user and return string adding first 2 and last 2 charcters of input string.

Input_string = str (input ("Enter String : "))

length = Input_string.__len__()

Output_string = Input_string[:2] + Input_string[length-2:]

print ("Output is : " + Output_string)



