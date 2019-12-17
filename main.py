categories = ["Phone", "Phone", "Phone", "Phone", "Phone", "Phone", "Tablet", "Tablet", "Tablet", "Tablet", "SIM card", "SIM card", "Case", "Case", "Charger", "Charger"]
itemcodes = ["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTLM", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM"]
descs = ["Compact", "Clam Shell", "RoboPhone – 5-inch screen and 64 GB memory", "RoboPhone – 6-inch screen and 256 GB memory", "Y-Phone Standard – 6-inch screen and 64 GB memory", "Y-Phone Deluxe – 6-inch screen and 256 GB memory", "RoboTab – 8-inch screen and 64 GB memory", "RoboTab – 10-inch screen and 128 GB memory", "Y-Tab Standard – 10-inch screen and 128 GB memory", "Y-Tab Deluxe – 10-inch screen and 256 GB memory", "SIM Free", "Pay As You Go", "Standard", "Luxury", "Car", "Home"]
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

useritem = ("Input the item code of the phone/tablet you want to buy.")
itemindex = itemcodes.index(useritem)
pricetotal += prices[itemindex]
append.itemspurchased(descs[itemindex])

simorPAYG = input("Do you want ")

