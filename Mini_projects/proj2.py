# Tip Calculator :

#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
cal_tip = tip / 100
total_tip = bill * cal_tip
total_bill = bill + total_tip

#Each person should pay (150.00 / 5) * 1.12 = 33.6
people_no = int(input("How many people to split the bill? "))
per_person_bill = total_bill / people_no
#Format the result to 2 decimal places = 33.60
final_amt = round(per_person_bill, 2)
print(f"Each person should pay : ${final_amt}")
