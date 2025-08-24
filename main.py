print("Welcome to pizza club\n To order follow the instructions")
size=input("Which size of pizza want to order S, M, L\n")
pepperoni=input("Do you want pepperoni?type y if yes otherwise type n \n")
cheese=input("Do you want extra cheese if yes type y or not want type n\n")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("typing error")
if pepperoni=="y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if cheese=="y":
    bill+=1
print(f"Total bill is ${bill}")













