

#accept two string from user and check if second string is rotation of first


print ("Enter first String : ")
input_str = str (input ())

print ("Enter rotation string to check: ")
rotation_str = str (input ())
   
temp = input_str + input_str

print ("output : " + str (rotation_str in temp))
