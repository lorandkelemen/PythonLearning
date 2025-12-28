print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Calculate tip amount and total
tip_amount = bill * (tip / 100)
total = bill + tip_amount

# Calculate per person amount
per_person = total / people

# Round to 2 decimal places
per_person = round(per_person, 2)

print(f"Each person should pay: ${per_person}")