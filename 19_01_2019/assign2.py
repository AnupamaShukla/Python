

#accept two string from user and check if second string is rotation of first


print ("Enter first String : ")
input_str = str (input ())
length1 = len(input_str)

print ("Enter rotation string to check: ")
rotation_str = str (input ())
length2 = len(rotation_str)

if length1 == length2 :
    
    temp = input_str + input_str

    if rotation_str in temp :
        print ("second string is rotation of first string")
    else :
        print ("second string is NOT rotation of first string")

else :
    print ("Invalid input")
