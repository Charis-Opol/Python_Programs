raining = input("is it raining? ")
raining = str.lower(raining)
if raining == "yes":
    windy = input("is it windy")
    wind = str.lower(windy)
    if windy == "yes":
        print("its too windy for an umbrella.")
    else:
        print("take an umbrella.")
else:
    print("enjoy your day")