print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? ')) *100
many_people = int(input('How many people to split the bill? '))
tip_porcentage = int(input('What porcentage tip would you like to give? 10, 12 or 15? ')) /100

bill_solver = ((bill + bill * tip_porcentage)/ many_people)/100
print(f"Each person should pay ${round(bill_solver,2)}")
