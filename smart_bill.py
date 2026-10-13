print("="*50)
print("KERALA FRESH MART".center(50))
print("SMART BILLING".center(50))
print("="*50)
customerName = input("Customer Name: ")
itemName = input("Item Name: ")
quantity = int(input("Quantity: "))
price = int(input("Price per unit (Rs): "))
loyalty = input("Loyalty member? (y/n): ")
paymentMode = input("Payment mode (cash/upi/card): ")
category = int(input("Category (1=Essential, 2=Grocery, 3=Other): "))
amount = quantity * price
if (amount>=2000):
    discount_rate = 10
elif (amount>=1000 and amount<2000):
    discount_rate = 5
elif (amount>=500 and amount<1000):
    discount_rate = 2
else:
    discount_rate = 0
discount = amount*discount_rate/100 
if (loyalty.lower()=="y" and amount>=500):
    loyalty_bonus = 25
else:
    loyalty_bonus = 0    
taxable_amount = amount - discount - loyalty_bonus
if (category==1):
    gst_rate = 0
elif (category==2):
    gst_rate = 5
else:
    gst_rate = 18
gst_amount = taxable_amount*gst_rate/100
grand_total = taxable_amount + gst_amount
print("\n")
print(f"{"Customer : "}{customerName:<50}")
print(50*"-")
print(f"{"Item":<20}{"Qty":^5}{"Price":>10}{"Amount":>15}")
print(f"{itemName:<20}{quantity:^5}{price:>{10},.2f}{amount:>{15},.2f}")
print("-"*50)
print(f"{"Amount:":<25}{amount:>{25},.2f}")
print(f"{"Discount rate:":<25}{discount_rate:>24}%")
print(f"{"Discount:":<25}{discount:>{25},.2f}")
print(f"{"Loyalty bonus:":<25}{loyalty_bonus:>{25},.2f}")
print(f"{"Taxable amount:":<25}{taxable_amount:>{25},.2f}")
print(f"{"GST rate:":<25}{gst_rate:>24}%")
print(f"{"GST amount:":<25}{gst_amount:>{25},.2f}")
print(f"{"Grand Total:":<25}{grand_total:>{25},.2f}")
print("="*50)
if ((quantity%12)==0):
    print(f"{"Bonus : free cloth bag with this order!":<50}")
if (grand_total>10000 and paymentMode.lower() == "cash"):
    print(f"{"Cash limit of Rs.10,000 exceeded. Pleas pay by UPI or card.":<50}")
elif (paymentMode.lower() in ("cash", "upi", "card")):
    print(f"{"Payment accepted via "}{paymentMode.upper():<50}")
else:
    print(f"{"Invalid payment mode":<50}")