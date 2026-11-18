'''
Calculate an electricity bill based on the following units as a run time input
first 100 units Rs.2 per unit
Next 100 units Rs.3 per unit
Above 200 units Rs.5 per unit
'''
unit= int(input("Enter you electricity unit:"))
if unit == 0:
    print('No electricity consumed. Charge: Rs. 0')
elif unit <= 100:
    charge = unit * 2
    print('Charge: Rs.', charge)
elif unit <= 200:
    charge = 100 * 2 + (unit - 100) * 3
    print('Charge: Rs.', charge)
elif unit < 0:
    print("Not a valid input")
else:
    charge = 100 * 2 + 100 * 3 + (unit - 200) * 5
    print('Charge: Rs.', charge)

