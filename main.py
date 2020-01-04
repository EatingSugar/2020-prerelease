categories = ["Phone", "Phone", "Phone", "Phone", "Phone", "Phone", "Tablet", "Tablet", "Tablet", "Tablet", "SIM card", "SIM card", "Case", "Case", "Charger", "Charger"]
itemcodes = ["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTLM", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM"]
descs = ["Compact", "Clam Shell", "RoboPhone – 5-inch screen and 64 GB memory", "RoboPhone – 6-inch screen and 256 GB memory", "Y-Phone Standard – 6-inch screen and 64 GB memory", "Y-Phone Deluxe – 6-inch screen and 256 GB memory", "RoboTab – 8-inch screen and 64 GB memory", "RoboTab – 10-inch screen and 128 GB memory", "Y-Tab Standard – 10-inch screen and 128 GB memory", "Y-Tab Deluxe – 10-inch screen and 256 GB memory", "SIM Free", "Pay As You Go", "Standard", "Luxury", "Car charger", "Home charger"]
prices = [29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149,99, 299.99, 499.99, 599.99, 0, 9.99, 0, 50, 19.99, 15.99]
pricetotal = 0
itemspurchased = []

phoneortablet = input("Do you want a 'phone' or 'tablet'? ")
while phoneortablet != "phone" and phoneortablet != "tablet":
  phoneortablet = input("Do you want a 'phone' or 'tablet'? ")

if phoneortablet == "phone":
  print("You can choose from: ")
  for item in range(6):
    print(descs[item] + " for $" + str(prices[item]))
    print("Item code: " + itemcodes[item])
    print()
else:
  print("You can choose from: ")
  for item in range(4):
    print(descs[item + 6] + " for $" + str(prices[item + 6]))
    print("Item code: " + itemcodes[item + 6])
    print()

useritem = input("Input the item code of the phone/tablet you want to buy. ")
itemindex = itemcodes.index(useritem)
pricetotal += prices[itemindex]
itemspurchased.append(descs[itemindex])

simorPAYG = input("Do you want 'SIM Free' or 'Pay As You Go'? ")
while simorPAYG != "SIM Free" and simorPAYG != "Pay As You Go":
  simorPAYG = input("Do you want a 'SIM' or 'Pay As You Go'? ")

simindex = descs.index(simorPAYG)
pricetotal += prices[simindex]
itemspurchased.append(descs[simindex])

casechoice = input("'Standard' or 'Luxury' case? ")
while casechoice != "Standard" and casechoice != "Luxury":
  casechoice = ("'Standard' or 'Luxury' case? ")

caseindex = descs.index(casechoice)
pricetotal += prices[caseindex]
itemspurchased.append(descs[caseindex])

numberofchargers = int(input("How many chargers? Input '0' for none, '1' for a car charger, '2' for a home charger,  or '3' for both. "))
while numberofchargers not in range(0, 3):
  numberofchargers = int(input("How many chargers? Input '0' for none, '1' for a car charger, '2' for a home charger,  or '3' for both. "))

if numberofchargers == 0:
  pass
elif numberofchargers == 3:
  itemspurchased.append(descs[14])
  itemspurchased.append(descs[15])
  pricetotal += (prices[14] + prices[15])
else:
  itemspurchased.append(descs[numberofchargers + 13])
  pricetotal += prices[numberofchargers + 13]

print("Total price: $" + str(pricetotal))
print("Items purchased: " + str(itemspurchased))
  
  




