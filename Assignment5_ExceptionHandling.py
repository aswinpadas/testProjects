def divCalc(a,b):
    try:
        ans=a/b
        return ans
    except:
        return "Somthing Wrong, Plz enter the correct values"

try:
    a = int(input("Enter the First number : "))
    b = int(input("Enter the Second number : "))
    print("Result : ", divCalc(a, b))
except:
    print("Invalid input")

#Output:

# Enter the First number : 20
# Enter the Second number : 0
# Result :  Somthing Wrong, Plz enter the correct values

# Enter the First number : 20
# Enter the Second number : 2
# Result :  10.0

# Enter the First number : 20
# Enter the Second number : abc
# Invalid input