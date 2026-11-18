# This program calculates the length of two messages entered by the user.
message1 = input("Enter the first message: ")
print("The length of the first message is: ", len(message1))
message2 = input("Enter the second message: ")
print("The length of the second message is: ", len(message2))

mark= 75
passed= mark >= 50
print("Did the student pass? ", passed)
print(type(passed))

fruit_names= ["apple", "banana", "cherry", "orange"]
print(fruit_names)
print(type(fruit_names))
print("There are", len(fruit_names), "fruits in the list.")

color_names= ("black","white","red","blue")
print(color_names)
print("There are", len(color_names), "colors in the tuple.")
print(type(color_names))
