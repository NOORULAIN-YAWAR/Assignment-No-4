# **************QUESTION NO 1**************
age= int(input("ENTER YOUR AGE : "))

if (age < 13) :
    print ("******* You are a child ******* ")

elif (age >=13) and (age<=19) :
    print ("******* You are  a teenager *******")

elif (age >=20) and (age <=59):
    print ("******* You are an adult *******")

elif (age >=60) :
    print ("******* You are a senior ******* ")
print("")
# **************QUESTION NO 2**************
print("Enter a number below to find that the number is -ve ,+ve or zero; ")
num =int(input("ENTER A NUMBER : "))

if (num < 0) :
    print (" ******* This is a negative number *******")
elif (num > 0):
    print ("*******This is a positive number *******")
elif (num ==0) :
    print ("******* The number is zero *******")
print("")
# **************QUESTION NO 3**************
#               part (i)
number_list =[ 10,20,30,40,50,60,70,80,90]

print (" { first Item of a number list :",number_list[0],"}")
print (" { last item of a number list : ",number_list[-1],"}")

#                part (ii)
print ("Number List =" ,number_list)
for i in number_list:
    print (i)

# **************QUESTION NO 4**************
dict={
"Course_name": "python",
"Duration"   :  "3 months",
"No.of.classes" : "24",

}
dict.update({"Teacher ":"Sir Fahad"})
print (dict)
 