weight=float(input("Enter weight: "))
height=float(input("Enter height: "))
height_cm=height/100
BMI_cal = weight / (height_cm ** 2)
print(f"Your BMI is: {BMI_cal:.2f}")

if BMI_cal < 18.5:
    print("Underweight")
elif BMI_cal < 25:
    print("Normal")
else:
    print("Overweight")


