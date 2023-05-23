subtotal = 0
gift_wrap_fee=0
dis = 0

products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

q1= int(input("Enter the quantity of Product A : "))
q2= int(input("Enter the quantity of Product B : "))
q3= int(input("Enter the quantity of Product C : "))

g1 = input("Is A wrapped as a gift? (y/n): ").lower()
g2 = input("Is B wrapped as a gift? (y/n): ").lower()
g3 = input("Is C wrapped as a gift? (y/n): ").lower()

#Gift Wrap Charges
if g1=='y':
    gift_wrap_fee+=q1
if g2=='y':
    gift_wrap_fee+=q2
if g3=='y':
    gift_wrap_fee+=q3
    
#Subtotal
print("Product  Quantity  price")
subtotal += q1 * 20
print("Product A ",q1,"  ",q1*products["Product A"])
subtotal += q2 * 40
print("Product B ",q2,"  ",q2*products["Product B"])

subtotal += q3 * 50
print("Product C ",q3,"  ",q3*products["Product C"])

print("Subtotal : ",subtotal)

#Shipping Fee
ship_fee = 5
ship_fee += ((q1+q2+q3)//10) *5


    
#Discounts
def flat_10(): 
    if q3 >10:
        dis = (.5 * q3*50)
    elif q2 >10:
        dis =(.5 * q2*40)
    elif q1 >10:
        dis = (.5 * q1*20)
    return dis

def tiered_50_discount(): 
    if q3 >15:
        dis = (.5 * (q3-15)*50)
    if q2 >15:
        dis =  (.5 * (q2-15)*40)
    if q1 >15:
        dis = (.5 * (q1-15)*20)
    return dis


if q1+q2+q3>30 and (q1>15 or q2>15 or q3>15):
    print("Discount Applied : tiered_50_discount")
    dis = tiered_50_discount()
elif q1+q2+ q3 >20:
    print("Discount Applied : bulk_10_discount")
    dis =  (subtotal*.1)
elif q1>10 or q2>10 or q3>10:
    print("Discount Applied : bulk_5_discount")
    dis = flat_10()
elif subtotal >200:
    print("Discount Applied : flat_10_discount")
    dis = 10

#total amount
total = subtotal-dis + gift_wrap_fee+ship_fee

print("Discount amount : ",dis)
print("Gift wrap fee : ",gift_wrap_fee)
print("Shipping fee : ",ship_fee)
print("Total : ",total)