num = 10 
while num > 0: 
    print(f"There are {num} greens bottles hanging on the wall.\nIf one bottle accidentall falls")
    answer = int(input("How many bottles will be hanging on the wall: "))
    num = num - 1
    if answer == num:
        print(f"There will be {num} green bottles hanging on the wall.")
    else:
        while answer != num:
            answer= int(input("No, try again: "))

    print("There are no more green bottles hanging on the wall.")

