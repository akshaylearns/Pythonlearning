mark={"Akshay":45,
      "Sree":65,
      "sara":75,
      "Ben":75}
highest=[]
for name,mark1 in mark.items():
    if mark1==max(mark.values()):
        highest.append(name) 
print(*highest)