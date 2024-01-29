from datetime import datetime


name = input("Enter the name : ")
#list of the items
lists='''
Rice   RS 20/kg
Sugar  Rs 30/kg
salt   Rs 20/Kg
oil    Rs 80/Liter
paneer Rs 110/Kg
maggi  Rs 50/pag
Boost  Rs 90/each
colgate Rs 87/each
'''
#declartion
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]#itemlist
qlist=[]#quantitylist
plist=[]#pricelist


#rates for the items
items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,'boost':90,'colgate':87}

option=int(input("for list of items press 1: "))
if option==1:
    print(lists)

for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or 2 exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice = totalprice+price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice 
        else:
            print("sorry you entered item is not available")
    else:
        print("you enter wrong number")
    inp=input("Can i bill the items yes or no :")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Vivek Supermarket",25*"=")
            print(28*" ","Hyderabad")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range (len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',totalprice)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visitin")
            print(75*"-")






















