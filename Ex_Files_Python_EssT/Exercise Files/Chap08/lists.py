Height = float(input("Enter your height in centimeters (cm): "))
Weight = float(input("Enter your Weight in kilograms (kg): "))
Height = Height / 100
BMI = Weight / (Height * Height)
print("Your Body Mass Index is: {}".format(BMI))
if (BMI > 0):
    if (BMI <= 16):
        print("Severely underweight")
    elif (BMI <= 18.5):
        print("Underweight")
    elif (BMI <= 25):
        print("Healthy")
    elif (BMI <= 30):
        print("Overweight")
    else:
        print("Severely overweight")
else:
    ("Enter valid details")
