# initialising various categories for the 20 products
categories = ["Phone", "Phone", "Phone", "Phone", "Phone", "Phone", "Tablet", "Tablet", "Tablet", "Tablet", "SIM card", "SIM card", "Case", "Case", "Charger", "Charger"] 
itemcodes = ["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTLM", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM"] 
descs = ["Compact", "Clam Shell", "RoboPhone – 5-inch screen & 64 GB memory", "RoboPhone – 6-inch screen & 256 GB memory", "Y-Phone Standard – 6-inch screen & 64 GB memory", "Y-Phone Deluxe – 6-inch screen & 256 GB memory", "RoboTab – 8-inch screen & 64 GB memory", "RoboTab – 10-inch screen & 128 GB memory", "Y-Tab Standard – 10-inch screen & 128 GB memory", "Y-Tab Deluxe – 10-inch screen & 256 GB memory", "SIM Free", "Pay As You Go", "Standard case", "Luxury case", "Car charger", "Home charger"] 
prices = [29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149,99, 299.99, 499.99, 599.99, 0, 9.99, 0, 50, 19.99, 15.99] 

# initialising a variable to track overall user cost of products
overallpricetotal = 0.0 

# initialising array to hold purchased items' descriptions
itemspurchased = [] 

# initialising integer to hold number of phones bought
phonesbought = 0

# initialising boolean variable to hold whether the user wants additional devices or not
additionaldevices = True 

# initialising constants for start & end index of phones in categories
STARTOFPHONES = categories.index("Phone")
ENDOFPHONES = STARTOFPHONES + categories.count("Phone")

# initialising while loop to run while the user still wants devices which contains the "buying" phase of the code
while additionaldevices == True:
  # initialising total price of current phone as a 0 value float
  pricetotal = 0.0 
  
  # printing prices, names & item codes of all devices
  print("You can choose from: \n") 
  for item in range(10): 
    print(descs[item] + "\n$" + str(prices[item]) + "\nItem code: " + itemcodes[item] + "\n") 
  
  # asking user for item code of device they want
  useritem = input("Input the item code of the phone/tablet you want to buy. \n") 
  while useritem not in itemcodes: 
    useritem = input("Error: unrecognised item code. Input the item code of the phone/tablet you want to buy. \n") 
  
  # adding price of phone to total price & appending name to items purchased array
  pricetotal += prices[itemcodes.index(useritem)]  
  itemspurchased.append(descs[itemcodes.index(useritem)]) 
  
  # knocking 10% off the device price if 1 or more devices have been bought
  pricetotal *= 0.9 if phonesbought > 0 else 1
  
  # if device purchased is a phone this code runs
  if useritem in itemcodes[STARTOFPHONES:ENDOFPHONES]: 
    # ask user whether they want sim free or payg
    simorPAYG = input("Do you want 'SIM Free' or 'Pay As You Go'? \n") 
    while simorPAYG != "SIM Free" and simorPAYG != "Pay As You Go": 
      simorPAYG = input("Error: incorrect option. Do you want 'SIM Free' or 'Pay As You Go'? \n") 

    # adding price of choice to total price & appending choice name to items purchased array
    pricetotal += prices[descs.index(simorPAYG)] 
    itemspurchased.append(simorPAYG) 
  
  # ask user whether they want standard or luxury case
  casechoice = input("'Standard case' or 'Luxury case'? \n") 
  while casechoice != "Standard case" and casechoice != "Luxury case": 
    casechoice = input("Error: incorrect option. 'Standard case' or 'Luxury case'? \n") 
  
  # adding price of choice to total price & appending choice name to items purchased array
  pricetotal += prices[descs.index(casechoice)] 
  itemspurchased.append(casechoice) 
  
  # ask user how many chargers they want
  numberofchargers = int(input("How many chargers? Input '0' for none, '1' for a car charger, '2' for a home charger, or '3' for both. \n")) 
  while numberofchargers not in range(0, 4): 
    numberofchargers = int(input("Error: must enter number between 0 & 3 inclusive. How many chargers? Input '0' for none, '1' for a car charger, '2' for a home charger, or '3' for both. \n")) 
  
  # appending price & descs of chargers chosen
  if numberofchargers == 3: 
    itemspurchased.append(descs[14:16]) 
    pricetotal += (prices[14] + prices[15]) 
  elif numberofchargers in range(1,3): 
    itemspurchased.append(descs[numberofchargers + 13])
    pricetotal += prices[numberofchargers + 13] 
  
  # checking if user wants an extra phone
  extraphone = input("Do you want an extra phone? [Y/N] \n") 
  while extraphone != "Y" and extraphone != "N": 
    extraphone = input("Error: Answer must be 'Y' or 'N'. Do you want an extra phone? [Y/N] \n") 
  
  # if user doesn't want an extra phone the loop ends & vice versa
  additionaldevices = False if extraphone == "N" else True
  
  # adding current phone total to overall total
  overallpricetotal += pricetotal 

# printing price total & items bought
print("Total price: $%s\nItems purchased: %s"%(overallpricetotal, itemspurchased)) 