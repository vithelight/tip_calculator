print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
bill_with_tip = total_bill * (1 + tip / 100)
for_each = bill_with_tip / people


print(f'Each person should pay: ${for_each:.2f}\n')
