print("Welcome to the tip calculator!\n")

total = float(input("How much was the total bill? $"))
tip_amt = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

bill_with_tip = total * (1 + tip_amt / 100)

amt_per_person = round((bill_with_tip / num_people), 2)

print(f"Each person needs to pay: ${amt_per_person}")