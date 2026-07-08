yr=int(input("Enter year"))
if yr%100==0 and yr%400==0:
    print("Leap year")
elif yr%4==0 and yr%100!=0:
    print("Leap year")
else:
    print("Not leap yr")