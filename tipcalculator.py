print("Welcome to the tip calculator")

totalBill = float(input("What was the total Bill? $"))
yourTip = float(input("How much tip would you like to give? 10, 12, or 15 ?"))
totalPeople = int(input("How many people to split the bill? "))

perPerson=totalBill*(1+yourTip/100)/totalPeople
print(f"Each person should pay: $, {perPerson:.2f}")