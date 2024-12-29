print("1) Square \n2) Triangle \n")
choice = int(input("Enter a number: "))
if choice == 1:
    side = int(input("Enter the length of one of the sides: "))
    area_square = side ** 2
    print(area_square)
elif choice == 2: 
    base = int(input("Enter the length of the base of the triangle: "))
    height = int(input("Enter the lenght of the height of the triangle: "))
    area_triangle = 0.5 * base * height
    print(area_triangle)
else: 
    print("Invalid choice")