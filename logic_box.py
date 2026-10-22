print("Welcome to the Pattern Generator and Number Analyzer!")
print()
print("select an option:")
print("1. generate a pattern")
print("2. analyze a range of numbers")
print("3. exit")
choice = input("enter your choice")
if choice == "1":
   rows = int(input("enter the number of rows"))
   for i in range(1, rows + 1):
        print("*" * i)
elif choice == "2":
    start = int(input("enter the start of the range:"))

    end = int(input("enter the end of the range:"))
    total = 0
    
    for num in range(start,end + 1):
        if num % 2 == 0:
           print(num, "is even")
        else:
           print(num, "is odd")
        total = total + num

    print("sum:", total)

elif choice == "3":
    print("thank you for using logic box!")
