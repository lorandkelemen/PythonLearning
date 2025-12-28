print("welcome")
size = input("What size pizza? S, M or L:")
pepperoni = input("Want pepperoni? Y or N:")
extra_cheese = input("Want extra cheese? Y or N:")

Smallprice =15
Mediumprice =20
Largeprice =25


if size == "S":
    finalprice = Smallprice
elif size == "M":
    finalprice = Mediumprice
else :
    finalprice = Largeprice

if pepperoni == "Y":
    finalprice = finalprice + 2

if extra_cheese == "Y":
    finalprice = finalprice + 1


print(f"final price is {finalprice}")