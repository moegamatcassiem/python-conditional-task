#JHB Metro Police
print("What was your average speed?: ")
km = input()

print("Speed limit: ")
sl = input()

if int(km) <= int(sl):
    print("ok")

elif int(km) == int(sl) + 5:
    print("1 point")
elif int(km) == int(sl) + 10:
    print("2 points")
elif int(km) == int(sl) + 15:
    print("3 points")
elif int(km) == int(sl) + 20:
    print("4 point")
elif int(km) == int(sl) + 25:
    print("5 points")
elif int(km) == int(sl) + 30:
    print("6 points")
elif int(km) == int(sl) + 35:
    print("7 point")
elif int(km) == int(sl) + 40:
    print("8 points")
elif int(km) == int(sl) + 45:
    print("9 points")
elif int(km) == int(sl) + 50:
    print("10 point")
elif int(km) == int(sl) + 55:
    print("11 points")
elif int(km) == int(sl) + 60:
    print("12 points")

if int(km) > int(sl) + 60:
    print("Time to go to jail!")
