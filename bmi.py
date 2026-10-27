# BMI Calculator

weight = float(input("Enter Weight in kgs: "))
height = float(input("Enter Height in m: "))

bmi = weight / (height ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are Underweight")
elif bmi <= 24.9:
    print("You are Healthy Weight")
elif bmi <= 29.9:
    print("You are Overweight")
elif bmi <= 34.9:
    print("You are Obesity (Class I)")
elif bmi <= 39.9:
    print("You are Obesity (Class II)")
else: # 40.0 or higher
    print("You are Severe Obesity (Class III)")