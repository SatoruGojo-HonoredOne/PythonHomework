firstcolor="red" 
c="orange"
color3="yellow"
c4="green"
_c="blue"
_color="indigo"
print(firstcolor, c, color3, c4, _c, _color)


#Same as first code but use input to get the colors of the rainbow from the user and print them out in order.

firstcolor=input("first color of the rainbow: ")
c=input("second color of the rainbow: ")
color3=input("third color of the rainbow: ")
c4=input("fourth color of the rainbow: ")
_c=input("fifth color of the rainbow: ")
_color=input("sixth color of the rainbow: ")
print("The colors of the rainbow are: ", firstcolor, c, color3, c4, _c, _color)


#create python code to perform basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.
print("This program will perform basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.")
a=int(input("first number: "))
b=int(input("second number: "))
c= a + b
d= a - b
e= a * b
f= a / b
print("sum is: ", c)
print("difference is: ", d)
print("product is: ", e)
print("quotient is: ", f)

#Create a python program that takes user input for their name, initials, grade, school name, favorite hobby, and city they live in. Then print out the type of each variable.
name= input("What is your name?")
initials= input("What are your initials?")
grade= input("What is your grade?")
school= input("What is your school name?")
hobby= input("What is your favorite hobby?")
city= input("What city do you live in?")
print("The type of name is: ", type(name))
print("The type of initials is: ", type(initials))
print("The type of grade is: ", type(grade))
print("The type of school is: ", type(school))
print("The type of hobby is: ", type(hobby))
print("The type of city is: ", type(city))

