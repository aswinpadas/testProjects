def bmiCalc(w,h):
    bmi=w/(h**2)
    return bmi

w=float(input("Enter your Weignt (in Kg) : "))
h=float(input("Enter your Height (in Meters) : "))
print("The BMI of the person :",bmiCalc(w,h))

#Output
# Enter your Weignt (in Kg) : 72
# Enter your Height (in Meters) : 1.56
# The BMI of the person : 29.585798816568044
