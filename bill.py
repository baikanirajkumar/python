print("D MART")
#let us assume there is only below items in mart
sugar=10
one_kg_sugarcost=45
biscuitpackets=10
one_biscuitpacket_cost=10
chocolatepackets=50
one_chocolate_cost=5
def buy_items():
    global sugar, biscuitpackets, chocolatepackets
    print("Avenue Supermart limited")
    select=input("enter multiple items:").split(" ")
    if '3' in select and '2' in select and '1' in select:
        sugar-=2
        biscuitpackets-=3
        chocolatepackets-=5
        totalamount=one_kg_sugarcost*2
        print(f"2kg Sugar = Rs{totalamount}")
        totalamountbiscuit=3*one_biscuitpacket_cost
        print(f"3 biscits = Rs{totalamountbiscuit}")
        totalchocolatescost=5*one_chocolate_cost
        print(f"5 chocolates = Rs{totalchocolatescost}")
        Totalcost=totalamount+totalamountbiscuit+totalchocolatescost
        print(f"Total cost = {Totalcost}")
        print("Thank you Visit Again")
        print("Happy Diwali")
    elif '1' in select and '2' in select:
        sugar-=2
        biscuitpackets-=3
        sugartotalamount=one_kg_sugarcost*2
        print(f"2kg Sugar = Rs{sugartotalamount}")
        totalamountbiscuit=3*one_biscuitpacket_cost
        print(f"3 biscits  = Rs{totalamountbiscuit}")
        amounttotal=sugartotalamount+totalamountbiscuit
        print(f"Total amount = {amounttotal}")
        print("Thank you visit Again")
        print("Happy diwali")       
buy_items()
print(f"available stock of sugar is :{sugar}")
print(f"available stock of chocolates is :{chocolatepackets}")
print(f"available stock of biscuitpackets is :{biscuitpackets}")





 



