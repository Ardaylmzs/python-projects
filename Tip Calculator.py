#tip calculator
print("welcome to the tip calculator!")
bill = float(input("enter the bill: "))
tip = int(input("enter the tip amount: "))
people = int(input("how many people? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"the total amount is: , ${final_amount}")
