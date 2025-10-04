temperature= int(input("Enter the temperature in Fahrenheit: "))
if temperature > 80:
    print("It's a hot day.")
elif 60 <= temperature <= 80:
    print("It's a pleasant day.")
else:
    print("It's a cold day.")